class Car:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):
        self.vMax = 50
        self.v0= 0
        self.p = 0.3
        self.d = 20
        
        self.x = 0
        self.v = self.v0
        
    def update(self, lead):
        if self.v + 10 <= self.vMax:
            self.v + 10
        