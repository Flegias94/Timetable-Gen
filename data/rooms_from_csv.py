from models.entities import Room


def load_rooms():
    return [
        Room(id="E101", capacity=70, features=["curs"]),
        Room(id="INCUBAF", capacity=20, features=["seminar"]),
        Room(id="Aula", capacity=150, features=["curs"]),
        Room(id="A033", capacity=20, features=["laborator"]),
        Room(id="A036a", capacity=20, features=["laborator"]),
        Room(id="A109", capacity=30, features=["seminar"]),
        Room(id="A110", capacity=20, features=["laborator"]),
        Room(id="A013", capacity=20, features=["seminar"]),
        Room(id="S.Club", capacity=40, features=["seminar"]),
        Room(id="E118", capacity=30, features=["seminar"]),
        Room(id="FIM1", capacity=110, features=["curs"]),
        Room(id="E123", capacity=20, features=["laborator"]),
        Room(id="E005", capacity=120, features=["curs"]),
        Room(id="H001", capacity=20, features=["seminar"]),
        Room(id="E233", capacity=110, features=["curs"]),
        Room(id="E119", capacity=30, features=["seminar"]),
        Room(id="E126", capacity=30, features=["seminar"]),
        Room(id="ED011", capacity=30, features=["seminar"]),
        Room(id="ED015", capacity=30, features=["seminar"]),
        Room(id="ED030", capacity=30, features=["seminar"]),
        Room(id="REZERVA", capacity=110, features=["curs"]),
        Room(id="REZSEM", capacity=40, features=["seminar"]),
    ]
