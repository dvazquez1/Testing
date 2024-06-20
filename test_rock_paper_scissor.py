from rock_paper_scissor import Participant, GameRound

def test_participant_incrementPoint():
    p = Participant("Test")
    p.incrementPoint()
    assert p.points == 1