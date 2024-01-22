class Computer:
    def set_spac(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')

print("데스크탑")
desktop = Computer()
# print(desktop)
desktop.set_spac("i7", "16GB", "GTX1060", "512GB")
desktop.hardware_info()

print()
print("노트북")
notebook = Computer()
# print(desktop)
notebook.set_spac("i5", "8GB", "MX300", "256GB")
notebook.hardware_info()

