from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

# RF01 — caixa preta / fronteiras
def test_usuario_valido_pode_emprestar():
    assert pode_emprestar(True, False, 0) is True

def test_usuario_inativo_nao_pode_emprestar():
    assert pode_emprestar(False, False, 0) is False

def test_usuario_com_pendencia_nao_pode_emprestar():
    assert pode_emprestar(True, True, 0) is False

def test_usuario_com_dois_emprestimos_pode_emprestar():
    assert pode_emprestar(True, False, 2) is True

def test_usuario_no_limite_de_tres_emprestimos_nao_pode_emprestar():
    # Este teste deve falhar com a implementação entregue,
    # revelando o defeito do RF01.
    assert pode_emprestar(True, False, 3) is False

def test_usuario_com_quatro_emprestimos_nao_pode_emprestar():
    assert pode_emprestar(True, False, 4) is False


# RF02 — valores de fronteira
def test_multa_zero_dias():
    assert calcular_multa(0) == 0.0

def test_multa_dias_negativos():
    assert calcular_multa(-1) == 0.0

def test_multa_um_dia():
    assert calcular_multa(1) == 2.0

def test_multa_sete_dias():
    assert calcular_multa(7) == 14.0

def test_multa_oito_dias():
    assert calcular_multa(8) == 17.0

def test_multa_dez_dias():
    assert calcular_multa(10) == 23.0


# RF03 — valores de fronteira
def test_classificacao_zero_dias():
    assert classificar_atraso(0) == "sem atraso"

def test_classificacao_um_dia():
    assert classificar_atraso(1) == "atraso leve"

def test_classificacao_sete_dias():
    assert classificar_atraso(7) == "atraso leve"

def test_classificacao_oito_dias():
    assert classificar_atraso(8) == "atraso moderado"

def test_classificacao_trinta_dias():
    assert classificar_atraso(30) == "atraso moderado"

def test_classificacao_trinta_e_um_dias():
    assert classificar_atraso(31) == "atraso grave"
