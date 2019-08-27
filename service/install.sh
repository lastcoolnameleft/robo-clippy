#!/usr/bin/env bash

cp clippy-button.service ~/.config/systemd/user/
cp clippy-listen.service ~/.config/systemd/user/

systemctl --user daemon-reload
systemctl --user enable clippy-button.service
systemctl --user restart clippy-button.service
systemctl --user enable clippy-listen.service
systemctl --user restart clippy-listen.service