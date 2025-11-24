def add_season(self, seasons_dict):
        """
        seasons_dict should look like:
        { 1: 10, 2: 8, 3: 12 }
        season_number = key
        episode_count = value
        """

        for season_number, episode_count in seasons_dict.items():

            season_box = QGroupBox(f"Season {season_number}")
            season_box.setObjectName("seasonBox")

            season_layout = QVBoxLayout()
            season_layout.setSpacing(6)

            for ep in range(1, episode_count + 1):

                ep_widget = QWidget()
                ep_widget.setObjectName("episodeWidget")
                ep_layout = QHBoxLayout(ep_widget)
                ep_layout.setContentsMargins(5, 2, 5, 2)

                # Episode label
                ep_label = QLabel(f"Episode {ep}")
                ep_label.setObjectName("episodeLabel")
                ep_layout.addWidget(ep_label)

                ep_layout.addStretch()

                # Eye icon
                eye_label = ClickableLabel()
                eye_label.setObjectName("eyeIcon")
                eye_label.setAlignment(Qt.AlignVCenter)

                eye_normal = ":/icons/Icons/eye.png"
                eye_seen = ":/icons/Icons/eye 1.png"

                # Set default icon
                eye_label.current_icon = eye_normal
                eye_label.setPixmap(
                    QPixmap(eye_label.current_icon).scaled(
                        18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation
                    )
                )

                # Toggle
                def make_toggle(lbl=eye_label):
                    def toggle():
                        lbl.current_icon = eye_seen if lbl.current_icon == eye_normal else eye_normal
                        lbl.setPixmap(
                            QPixmap(lbl.current_icon).scaled(
                                18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation
                            )
                        )
                    return toggle

                eye_label.clicked.connect(make_toggle())

                ep_layout.addWidget(eye_label)
                season_layout.addWidget(ep_widget)

            season_box.setLayout(season_layout)
            self.ui.main_layout.addWidget(season_box)
