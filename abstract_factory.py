from abc import ABC, abstractmethod


# interface for Car object
class ICar(ABC):
    @abstractmethod
    def assemble(self):
        pass

#concrete Car implementations
class Sedan(ICar):
    def assemble(self):
        print("Assembled a sedan!")


class Hatchback(ICar):
    def assemble(self):
        print("Assembled a hatchback!")

class SUV(ICar):
    def assemble(self):
        print("Assembled a SUV!")


#  interface for CarSpecification object
class ICarSpecification(ABC):
    @abstractmethod
    def display(self):
        pass

# concrete implementations

class EuropeCarSpecification(ICarSpecification):
    def display(self):
        print("This car is made for Europe.")


class NorthAmericaCarSpecification(ICarSpecification):
    def display(self):
        print("This car is made for North America.")


class AsiaCarSpecification(ICarSpecification):
    def display(self):
        print("This car is made for Asia.")


# Abstract CarFactory
class ICarFactory(ABC):
    @abstractmethod
    def create_car(self)->ICar:
        pass

    @abstractmethod
    def create_specs(self)-> ICarSpecification:
        pass

# concrete CarFactories (know which type of car ans specs are needed)

class EuropeCarFactory(ICarFactory):
    def create_car(self) ->ICar:
        return Sedan()

    def create_specs(self) -> ICarSpecification:
        return EuropeCarSpecification()


class NorthAmericaCarFactory(ICarFactory):
    def create_car(self) ->ICar:
        return SUV()

    def create_specs(self) -> ICarSpecification:
        return NorthAmericaCarSpecification()


class AsiaCarFactory(ICarFactory):
    def create_car(self) ->ICar:
        return Hatchback()

    def create_specs(self) -> ICarSpecification:
        return AsiaCarSpecification()


def client(car_factory: ICarFactory):
    prototype = car_factory.create_car()
    specs = car_factory.create_specs()
    prototype.assemble()
    specs.display()


if __name__ == "__main__":
    client(AsiaCarFactory())



