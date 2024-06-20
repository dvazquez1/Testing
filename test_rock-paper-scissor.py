from rock_paper_scissor import Participant, GameRound

def test_participant_initialization():
    p = Participant("Test")
    assert p.name == "Test"
    assert p.points == 0
    assert p.choice == ""

def test_participant_choose(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "rock")
    p = Participant("Test")
    p.choose()
    assert p.choice == "rock"

def test_participant_incrementPoint():
    p = Participant("Test")
    p.incrementPoint()
    assert p.points == 1

def test_game_round(monkeypatch):
    p1 = Participant("Player 1")
    p2 = Participant("Player 2")
    monkeypatch.setattr('builtins.input', lambda _: "rock")
    p1.choose()
    monkeypatch.setattr('builtins.input', lambda _: "scissor")
    p2.choose()
    round = GameRound(p1, p2)
    assert p1.points == 1
    assert p2.points == 0
