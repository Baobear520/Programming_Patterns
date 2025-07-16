import random
from abc import abstractmethod, ABC
from typing import List


class ISub(ABC):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    @abstractmethod
    def update(self, pub: 'IPublisher'):
        pass


class IPublisher(ABC):
    @abstractmethod
    def subscribe(self, sub: ISub) -> None:
        pass

    def unsubscribe(self, sub: ISub) -> None:
        pass

    def notify(self):
        pass


class Publisher(ABC):
    _subscribers: List[ISub] = []
    _event = None

    def subscribe(self, sub: ISub) -> None:
        self._subscribers.append(sub)
        print(f"{sub} has subscribed!")

    def unsubscribe(self, sub: ISub) -> None:
        self._subscribers.remove(sub)
        print(f"{sub} has unsubscribed! ")


    def _get_all_subscribers_list(self) -> List[ISub]:
        return self._subscribers

    def notify(self) -> None:
        for s in self._subscribers:
            s.update(self)
            print(f"Subscriber '{s.name}' has been notified!")

    def business_logic(self):
        self._event = random.randint(1,10)
        self.notify()



class WeatherSub(ISub):
    def update(self, pub: Publisher):
        if pub._event > 5:
            print(f"Got {pub._event}! Wohoo!")


class SportSub(ISub):
    def update(self, pub: Publisher):
        if pub._event > 5:
            print(f"Got {pub._event}!Yay!")


if __name__ == "__main__":

    sub1 = WeatherSub("TV 1")
    sub2 = WeatherSub("NBC")
    sub3 = SportSub("Sports 1")

    pub = Publisher()
    pub.subscribe(sub1)
    pub.subscribe(sub2)
    pub.subscribe(sub3)

    pub.business_logic()

    pub.unsubscribe(sub2)
    pub.unsubscribe(sub3)
    pub.business_logic()







