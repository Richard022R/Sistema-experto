import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QComboBox, QSpinBox, 
                             QPushButton, QTextEdit, QDoubleSpinBox, QGroupBox,
                             QCheckBox, QMessageBox, QFrame, QScrollArea, QDialog)
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt
from sistema_inversion import SistemaInversion, PerfilRiesgo

class VentanaBienvenida(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema Experto de Inversiones')
        self.setFixedSize(800, 500)
        self.setStyleSheet("""
            QDialog {
                background-color: #f0f2f5;
            }
            QLabel#titulo {
                font-size: 32px;
                font-weight: bold;
                color: #2c3e50;
                margin: 20px;
            }
            QLabel#subtitulo {
                font-size: 16px;
                color: #34495e;
                margin: 10px;
                line-height: 1.5;
            }
            QLabel#caracteristicas {
                font-size: 14px;
                color: #2c3e50;
                padding: 10px;
            }
            QPushButton#iniciar {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 15px 30px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton#iniciar:hover {
                background-color: #27ae60;
            }
            QPushButton#info {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px 30px;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton#info:hover {
                background-color: #2980b9;
            }
            QFrame#linea {
                background-color: #bdc3c7;
            }
        """)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Logo o Ícono (representado como texto estilizado)
        logo_label = QLabel("💰📊")
        logo_label.setStyleSheet("font-size: 48px; text-align: center;")
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        
        # Título Principal
        titulo = QLabel('Sistema Experto de Inversiones')
        titulo.setObjectName('titulo')
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)
        
        # Línea separadora
        linea = QFrame()
        linea.setObjectName('linea')
        linea.setFrameShape(QFrame.HLine)
        linea.setFixedHeight(2)
        layout.addWidget(linea)
        
        # Subtítulo/Descripción
        subtitulo = QLabel('Tu asistente inteligente para tomar decisiones financieras informadas')
        subtitulo.setObjectName('subtitulo')
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setWordWrap(True)
        layout.addWidget(subtitulo)
        
        # Características principales
        caracteristicas = QLabel("""
        ✓ Análisis personalizado de tu perfil de inversor
        ✓ Recomendaciones basadas en condiciones actuales del mercado
        ✓ Estrategias de inversión adaptadas a tus objetivos
        ✓ Evaluación de riesgos y oportunidades
        """)
        caracteristicas.setObjectName('caracteristicas')
        caracteristicas.setAlignment(Qt.AlignCenter)
        layout.addWidget(caracteristicas)
        
        # Espaciador
        layout.addStretch()
        
        # Contenedor para botones
        botones_layout = QHBoxLayout()
        botones_layout.setSpacing(20)
        
        # Botón Iniciar
        btn_iniciar = QPushButton('Comenzar Análisis')
        btn_iniciar.setObjectName('iniciar')
        btn_iniciar.setCursor(Qt.PointingHandCursor)
        btn_iniciar.clicked.connect(self.abrir_ventana_inversion)
        botones_layout.addWidget(btn_iniciar)
        
        # Botón Información
        btn_info = QPushButton('Más Información')
        btn_info.setObjectName('info')
        btn_info.setCursor(Qt.PointingHandCursor)
        btn_info.clicked.connect(self.mostrar_informacion)
        botones_layout.addWidget(btn_info)
        
        layout.addLayout(botones_layout)
        self.setLayout(layout)
        
    def abrir_ventana_inversion(self):
        self.ventana_inversion = VentanaInversion()
        self.ventana_inversion.show()
        self.close()
        
    def mostrar_informacion(self):
        QMessageBox.information(
            self,
            'Información del Sistema',
            '''<h3>Sistema Experto de Inversiones</h3>
            <p>Este sistema de asesoramiento financiero está diseñado para ayudarte a:</p>
            <ul>
                <li>Determinar tu perfil de riesgo como inversor</li>
                <li>Analizar las condiciones actuales del mercado</li>
                <li>Generar recomendaciones de inversión personalizadas</li>
                <li>Optimizar tu cartera de inversiones</li>
            </ul>
            <p>Utilizamos algoritmos avanzados y análisis experto para brindarte 
            las mejores recomendaciones según tu situación particular.</p>''',
            QMessageBox.Ok
        )

class VentanaInversion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sistema = SistemaInversion()
        self.initUI()
        self.aplicar_estilos()
        
    def aplicar_estilos(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 10px;
                background-color: #3498db;
                color: white;
                border-radius: 5px;
            }
            QLabel {
                font-size: 12px;
                color: #2c3e50;
            }
            QComboBox, QSpinBox, QDoubleSpinBox {
                padding: 5px;
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;
                min-height: 25px;
            }
            QPushButton {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
            QCheckBox {
                font-size: 12px;
                padding: 5px;
            }
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 10px;
                background-color: white;
                font-size: 13px;
            }
        """)

    def initUI(self):
        self.setWindowTitle('Sistema Experto de Inversiones')
        self.setGeometry(100, 100, 1000, 800)
        
        # Contenedor principal con scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)
        
        # Widget principal
        widget_principal = QWidget()
        scroll.setWidget(widget_principal)
        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(20)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        
        # Título principal
        titulo = QLabel('Sistema Experto de Asesoramiento Financiero')
        titulo.setStyleSheet("""
            font-size: 24px;
            color: #2c3e50;
            padding: 10px;
            font-weight: bold;
            qproperty-alignment: AlignCenter;
        """)
        layout_principal.addWidget(titulo)
        
        # Contenedor horizontal para formularios
        layout_formularios = QHBoxLayout()
        
        # Panel izquierdo
        panel_izquierdo = QVBoxLayout()
        
        # Grupo: Perfil del Inversor
        grupo_perfil = QGroupBox('Perfil del Inversor')
        layout_perfil = QVBoxLayout()
        layout_perfil.setSpacing(15)
        
        # Tolerancia al riesgo
        layout_riesgo = self.crear_campo_formulario('Tolerancia al riesgo:')
        self.combo_riesgo = QComboBox()
        self.combo_riesgo.addItems(['Conservador', 'Moderado', 'Agresivo'])
        layout_riesgo.addWidget(self.combo_riesgo)
        layout_perfil.addLayout(layout_riesgo)
        
        # Horizonte temporal
        layout_horizonte = self.crear_campo_formulario('Horizonte temporal:')
        self.combo_horizonte = QComboBox()
        self.combo_horizonte.addItems(['Corto plazo (1-2 años)', 
                                     'Medio plazo (3-5 años)', 
                                     'Largo plazo (>5 años)'])
        layout_horizonte.addWidget(self.combo_horizonte)
        layout_perfil.addLayout(layout_horizonte)
        
        # Experiencia previa
        layout_experiencia = self.crear_campo_formulario('Experiencia en inversiones:')
        self.combo_experiencia = QComboBox()
        self.combo_experiencia.addItems(['Principiante', 'Intermedio', 'Experto'])
        layout_experiencia.addWidget(self.combo_experiencia)
        layout_perfil.addLayout(layout_experiencia)
        
        grupo_perfil.setLayout(layout_perfil)
        panel_izquierdo.addWidget(grupo_perfil)
        
        # Panel derecho
        panel_derecho = QVBoxLayout()
        
        # Grupo: Detalles de Inversión
        grupo_detalles = QGroupBox('Detalles de Inversión')
        layout_detalles = QVBoxLayout()
        layout_detalles.setSpacing(15)
        
        # Monto
        layout_monto = self.crear_campo_formulario('Monto a invertir ($):')
        self.spin_monto = QDoubleSpinBox()
        self.spin_monto.setRange(1000, 10000000)
        self.spin_monto.setValue(100000)
        self.spin_monto.setSingleStep(1000)
        self.spin_monto.setGroupSeparatorShown(True)
        layout_monto.addWidget(self.spin_monto)
        layout_detalles.addLayout(layout_monto)
        
        # Plazo
        layout_plazo = self.crear_campo_formulario('Plazo (años):')
        self.spin_plazo = QSpinBox()
        self.spin_plazo.setRange(1, 30)
        self.spin_plazo.setValue(5)
        layout_plazo.addWidget(self.spin_plazo)
        layout_detalles.addLayout(layout_plazo)
        
        grupo_detalles.setLayout(layout_detalles)
        panel_derecho.addWidget(grupo_detalles)
        
        # Grupo: Condiciones de Mercado
        grupo_mercado = QGroupBox('Condiciones Actuales del Mercado')
        layout_mercado = QVBoxLayout()
        layout_mercado.setSpacing(10)
        
        self.check_inflacion = self.crear_checkbox('Alta inflación', 
            'Los precios están aumentando significativamente')
        self.check_recesion = self.crear_checkbox('Recesión', 
            'La economía está en contracción')
        self.check_crecimiento = self.crear_checkbox('Crecimiento económico', 
            'La economía está en expansión')
        
        layout_mercado.addWidget(self.check_inflacion)
        layout_mercado.addWidget(self.check_recesion)
        layout_mercado.addWidget(self.check_crecimiento)
        
        grupo_mercado.setLayout(layout_mercado)
        panel_derecho.addWidget(grupo_mercado)
        
        # Agregar paneles al layout horizontal
        layout_formularios.addLayout(panel_izquierdo)
        layout_formularios.addLayout(panel_derecho)
        
        # Agregar layout horizontal al principal
        layout_principal.addLayout(layout_formularios)
        
        # Botón Analizar
        self.btn_analizar = QPushButton('Analizar y Generar Recomendaciones')
        self.btn_analizar.setMinimumHeight(50)
        self.btn_analizar.clicked.connect(self.realizar_analisis)
        layout_principal.addWidget(self.btn_analizar)
        
        # Grupo: Resultados
        grupo_resultados = QGroupBox('Análisis y Recomendaciones')
        layout_resultados = QVBoxLayout()
        
        self.texto_resultados = QTextEdit()
        self.texto_resultados.setReadOnly(True)
        self.texto_resultados.setMinimumHeight(200)
        layout_resultados.addWidget(self.texto_resultados)
        
        grupo_resultados.setLayout(layout_resultados)
        layout_principal.addWidget(grupo_resultados)
        
        widget_principal.setLayout(layout_principal)

    def crear_campo_formulario(self, texto: str) -> QHBoxLayout:
        layout = QHBoxLayout()
        label = QLabel(texto)
        label.setMinimumWidth(150)
        layout.addWidget(label)
        return layout
        
    def crear_checkbox(self, texto: str, tooltip: str) -> QCheckBox:
        checkbox = QCheckBox(texto)
        checkbox.setToolTip(tooltip)
        return checkbox
        
    def obtener_valor_combo(self, combo):
        return combo.currentIndex() + 1
        
    def realizar_analisis(self):
        try:
            self.btn_analizar.setEnabled(False)
            self.btn_analizar.setText('Analizando...')
            
            # Recopilar respuestas del cuestionario
            respuestas_cuestionario = {
                'tolerancia_riesgo': self.obtener_valor_combo(self.combo_riesgo),
                'horizonte_temporal': self.obtener_valor_combo(self.combo_horizonte),
                'experiencia_previa': self.obtener_valor_combo(self.combo_experiencia)
            }
            
            # Obtener perfil
            perfil = self.sistema.evaluar_perfil(respuestas_cuestionario)
            
            # Recopilar condiciones de mercado
            condiciones_mercado = []
            if self.check_inflacion.isChecked():
                condiciones_mercado.append('alta_inflacion')
            if self.check_recesion.isChecked():
                condiciones_mercado.append('recesion')
            if self.check_crecimiento.isChecked():
                condiciones_mercado.append('crecimiento_economico')
            
            # Obtener recomendaciones
            recomendaciones = self.sistema.recomendar_inversiones(
                perfil=perfil,
                monto=self.spin_monto.value(),
                plazo=self.spin_plazo.value(),
                condiciones_mercado=condiciones_mercado
            )
            
            # Obtener explicación
            explicacion = self.sistema.explicar_recomendacion(
                recomendaciones,
                perfil,
                condiciones_mercado
            )
            
            # Mostrar resultados
            self.texto_resultados.setText(explicacion)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al procesar: {str(e)}')
        finally:
            self.btn_analizar.setEnabled(True)
            self.btn_analizar.setText('Analizar y Generar Recomendaciones')

def main():
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(240, 242, 245))
    app.setPalette(palette)
    
    # Mostrar la ventana de bienvenida primero
    ventana_bienvenida = VentanaBienvenida()
    ventana_bienvenida.exec_()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()