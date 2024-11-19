import networkx as nx
from typing import Dict, List, Tuple
from enum import Enum

class PerfilRiesgo(Enum):
    CONSERVADOR = 1
    MODERADO = 2
    AGRESIVO = 3

class SistemaInversion:
    def __init__(self):
        # Base de conocimientos de instrumentos financieros
        self.instrumentos = {
            'bonos_gubernamentales': {
                'riesgo': 0.1,
                'rendimiento_esperado': 0.05,
                'liquidez': 0.7,
                'plazo_minimo': 1,  # en años
                'perfil_recomendado': PerfilRiesgo.CONSERVADOR
            },
            'acciones_blue_chip': {
                'riesgo': 0.4,
                'rendimiento_esperado': 0.12,
                'liquidez': 0.9,
                'plazo_minimo': 3,
                'perfil_recomendado': PerfilRiesgo.MODERADO
            },
            'startups': {
                'riesgo': 0.8,
                'rendimiento_esperado': 0.25,
                'liquidez': 0.3,
                'plazo_minimo': 5,
                'perfil_recomendado': PerfilRiesgo.AGRESIVO
            },
            'fondos_mixtos': {
                'riesgo': 0.5,
                'rendimiento_esperado': 0.15,
                'liquidez': 0.6,
                'plazo_minimo': 2,
                'perfil_recomendado': PerfilRiesgo.MODERADO
            },
            'bienes_raices': {
                'riesgo': 0.6,
                'rendimiento_esperado': 0.18,
                'liquidez': 0.2,
                'plazo_minimo': 7,
                'perfil_recomendado': PerfilRiesgo.MODERADO
            }
        }
        
        # Reglas de inferencia para condiciones de mercado
        self.reglas_mercado = {
            'alta_inflacion': {
                'bonos_gubernamentales': -0.2,
                'acciones_blue_chip': 0.1,
                'startups': -0.1,
                'fondos_mixtos': 0.0,
                'bienes_raices': 0.3
            },
            'recesion': {
                'bonos_gubernamentales': 0.3,
                'acciones_blue_chip': -0.2,
                'startups': -0.4,
                'fondos_mixtos': -0.1,
                'bienes_raices': -0.2
            },
            'crecimiento_economico': {
                'bonos_gubernamentales': -0.1,
                'acciones_blue_chip': 0.3,
                'startups': 0.4,
                'fondos_mixtos': 0.2,
                'bienes_raices': 0.2
            }
        }
        
        # Inicializar red de decisión
        self.red_decision = nx.DiGraph()
        self._construir_red()
        
    def _construir_red(self):
        """Construye la red de decisión para el sistema experto"""
        # Nodos de perfil
        for perfil in PerfilRiesgo:
            self.red_decision.add_node(perfil.name, tipo='perfil')
            
        # Nodos de instrumentos
        for instrumento in self.instrumentos:
            self.red_decision.add_node(instrumento, tipo='instrumento')
            
        # Nodos de condiciones de mercado
        for condicion in self.reglas_mercado:
            self.red_decision.add_node(condicion, tipo='condicion_mercado')
            
        # Establecer relaciones
        for instrumento, info in self.instrumentos.items():
            perfil = info['perfil_recomendado'].name
            self.red_decision.add_edge(perfil, instrumento)
            
        for condicion in self.reglas_mercado:
            for instrumento in self.instrumentos:
                self.red_decision.add_edge(condicion, instrumento)

    def evaluar_perfil(self, respuestas: Dict[str, int]) -> PerfilRiesgo:
        """Evalúa el perfil del inversor basado en sus respuestas"""
        # Cálculo simplificado del perfil
        puntuacion = sum(respuestas.values()) / len(respuestas)
        
        if puntuacion < 2:
            return PerfilRiesgo.CONSERVADOR
        elif puntuacion < 3:
            return PerfilRiesgo.MODERADO
        else:
            return PerfilRiesgo.AGRESIVO

    def recomendar_inversiones(self, 
                             perfil: PerfilRiesgo,
                             monto: float,
                             plazo: int,
                             condiciones_mercado: List[str]) -> Dict[str, float]:
        """
        Genera recomendaciones de inversión basadas en el perfil y condiciones
        
        Args:
            perfil: Perfil de riesgo del inversor
            monto: Cantidad a invertir
            plazo: Plazo de inversión en años
            condiciones_mercado: Lista de condiciones económicas actuales
            
        Returns:
            Dict con la distribución recomendada del portafolio
        """
        recomendaciones = {}
        
        # Filtrar instrumentos por plazo y perfil
        instrumentos_validos = {
            nombre: info for nombre, info in self.instrumentos.items()
            if info['plazo_minimo'] <= plazo and
            info['perfil_recomendado'].value <= perfil.value + 1
        }
        
        # Calcular score base para cada instrumento
        for nombre, info in instrumentos_validos.items():
            score = 1.0
            
            # Ajustar por perfil
            if info['perfil_recomendado'] == perfil:
                score *= 1.2
                
            # Ajustar por condiciones de mercado
            for condicion in condiciones_mercado:
                if condicion in self.reglas_mercado:
                    score *= (1 + self.reglas_mercado[condicion][nombre])
            
            recomendaciones[nombre] = score
            
        # Normalizar para obtener porcentajes
        total = sum(recomendaciones.values())
        for instrumento in recomendaciones:
            recomendaciones[instrumento] = (recomendaciones[instrumento] / total) * monto
            
        return recomendaciones

    def explicar_recomendacion(self, 
                              recomendaciones: Dict[str, float],
                              perfil: PerfilRiesgo,
                              condiciones_mercado: List[str]) -> str:
        """Genera una explicación detallada de las recomendaciones"""
        explicacion = f"Recomendación para perfil {perfil.name}:\n\n"
        
        # Explicar distribución
        explicacion += "Distribución recomendada:\n"
        for instrumento, monto in recomendaciones.items():
            info = self.instrumentos[instrumento]
            explicacion += f"- {instrumento}: ${monto:,.2f}\n"
            explicacion += f"  Rendimiento esperado: {info['rendimiento_esperado']*100:.1f}%\n"
            explicacion += f"  Nivel de riesgo: {info['riesgo']*100:.1f}%\n\n"
        
        # Explicar condiciones de mercado
        if condiciones_mercado:
            explicacion += "\nFactores de mercado considerados:\n"
            for condicion in condiciones_mercado:
                explicacion += f"- {condicion}\n"
                
        return explicacion