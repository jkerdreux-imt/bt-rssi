
bt-rssi:main.c
	gcc main.c -lbluetooth -o bt-rssi

install:bt-rssi
	@echo "======================================="
	@echo "WARNING bt-rssi will setcap cap_net_raw"
	@echo "======================================="
	cp bt-rssi /usr/local/bin
	setcap cap_net_raw+ep /usr/local/bin/bt-rssi

uninstall:
	@echo "Uninstalling bt-rssi"
