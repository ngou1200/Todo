from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QComboBox, QSpinBox, QPushButton, QCheckBox,
                            QFileDialog)
from utils.config_manager import ConfigManager

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config = ConfigManager.get_instance()
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        self.setWindowTitle("Settings")
        layout = QVBoxLayout(self)

        # Theme settings
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["light", "dark"])
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        layout.addLayout(theme_layout)

        # Language settings
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Language:")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["en", "es", "fr", "de"])
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # Backup settings
        backup_layout = QHBoxLayout()
        backup_label = QLabel("Backup Interval (hours):")
        self.backup_spin = QSpinBox()
        self.backup_spin.setRange(1, 168)  # 1 hour to 1 week
        backup_layout.addWidget(backup_label)
        backup_layout.addWidget(self.backup_spin)
        layout.addLayout(backup_layout)

        # Backup location
        backup_loc_layout = QHBoxLayout()
        self.backup_loc_label = QLabel("Backup Location:")
        self.backup_loc_button = QPushButton("Choose Directory")
        self.backup_loc_button.clicked.connect(self.choose_backup_location)
        backup_loc_layout.addWidget(self.backup_loc_label)
        backup_loc_layout.addWidget(self.backup_loc_button)
        layout.addLayout(backup_loc_layout)

        # Notification settings
        notif_layout = QHBoxLayout()
        self.notif_check = QCheckBox("Enable Notifications")
        self.sound_check = QCheckBox("Enable Sound")
        notif_layout.addWidget(self.notif_check)
        notif_layout.addWidget(self.sound_check)
        layout.addLayout(notif_layout)

        # Reminder advance notice
        advance_layout = QHBoxLayout()
        advance_label = QLabel("Reminder Advance Notice (minutes):")
        self.advance_spin = QSpinBox()
        self.advance_spin.setRange(1, 60)
        advance_layout.addWidget(advance_label)
        advance_layout.addWidget(self.advance_spin)
        layout.addLayout(advance_layout)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_button.clicked.connect(self.save_settings)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def load_settings(self):
        # Load current settings from config
        self.theme_combo.setCurrentText(self.config.get("app.theme"))
        self.lang_combo.setCurrentText(self.config.get("app.language"))
        self.backup_spin.setValue(self.config.get("app.backup_interval"))
        self.backup_loc_label.setText(f"Backup Location: {self.config.get('app.backup_location')}")
        self.notif_check.setChecked(self.config.get("notifications.enabled"))
        self.sound_check.setChecked(self.config.get("notifications.sound"))
        self.advance_spin.setValue(self.config.get("notifications.advance_notice"))

    def choose_backup_location(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Choose Backup Directory",
            self.config.get("app.backup_location")
        )
        if directory:
            self.backup_loc_label.setText(f"Backup Location: {directory}")

    def save_settings(self):
        # Save settings to config
        self.config.set("app.theme", self.theme_combo.currentText())
        self.config.set("app.language", self.lang_combo.currentText())
        self.config.set("app.backup_interval", self.backup_spin.value())
        self.config.set("app.backup_location", self.backup_loc_label.text().replace("Backup Location: ", ""))
        self.config.set("notifications.enabled", self.notif_check.isChecked())
        self.config.set("notifications.sound", self.sound_check.isChecked())
        self.config.set("notifications.advance_notice", self.advance_spin.value())
        self.config.save_config()
        self.accept()