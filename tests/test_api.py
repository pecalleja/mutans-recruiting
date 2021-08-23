from http import HTTPStatus


def test_api_no_mutant(api_client, dna_human):
    result = api_client.post("/mutant", json={"dna": dna_human})
    assert result.status_code == HTTPStatus.FORBIDDEN


def test_api_recruit_this_mutant(api_client, dna_mutant):
    result = api_client.post("/mutant", json={"dna": dna_mutant})
    assert result.status_code == HTTPStatus.OK
