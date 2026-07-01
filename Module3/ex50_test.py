from ex50 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zombie", 1000, 1000)

    # these asserts are bad, fix them
    assert boxer.hp == 100, "Boxer has a Wrong HP"
    assert zombie.hp == 1000, "Zombie has a Wrong HP"

    boxer.hit(zombie)
    assert zombie.alive(), "Zobmie should be alive after being hit by boxer"

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead"
