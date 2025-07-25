import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QFileDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

class EmailTemplateEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HTML Email Template Editor')
        self.setGeometry(100, 100, 1000, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        editor_layout = QHBoxLayout()

        self.html_editor = QTextEdit()
        self.html_editor.setPlaceholderText('Write your HTML email template here...')

        self.preview = QWebEngineView()
        self.preview.setHtml('<h3>Email preview will appear here</h3>')

        editor_layout.addWidget(self.html_editor, 2)
        editor_layout.addWidget(self.preview, 3)

        button_layout = QHBoxLayout()
        load_btn = QPushButton('Load')
        save_btn = QPushButton('Save')
        preview_btn = QPushButton('Preview')

        load_btn.clicked.connect(self.load_template)
        save_btn.clicked.connect(self.save_template)
        preview_btn.clicked.connect(self.update_preview)

        button_layout.addWidget(load_btn)
        button_layout.addWidget(save_btn)
        button_layout.addWidget(preview_btn)

        layout.addLayout(editor_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_template(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open HTML Template', '', 'HTML Files (*.html);;All Files (*)', options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as f:
                self.html_editor.setPlainText(f.read())

    def save_template(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save HTML Template', '', 'HTML Files (*.html);;All Files (*)', options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(self.html_editor.toPlainText())

    def update_preview(self):
        html = self.html_editor.toPlainText()
        self.preview.setHtml(html)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailTemplateEditor()
    window.show()
    sys.exit(app.exec_())
