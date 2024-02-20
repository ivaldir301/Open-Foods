def formatProductNutriScore(productNutriScore: str) -> str:
    if 'A' in productNutriScore:
        return 'A'
    else:
        return 'score desconhecido'

def setProductNutriScoreTitle(productNutriScore: str) -> str:
    if 'Qualidade nutricional muito boa' in productNutriScore:
        return 'Qualidade nutricional muito boa'
    elif 'Nutri-Score desconhecido' in productNutriScore:
        return 'Nutri-Score desconhecido'
    
def formatProductNovaScore(productNovaScore: str) -> str:
    if 'A' in productNovaScore:
        return 'A'
    else:
        return 'score desconhecido'
    
def setProductNovaScoreTitle(productNovaScore: str) -> str:
    if 'Alimentos não processados' in productNovaScore:
        return 'Alimentos não processados'
    elif 'Nutri-Score desconhecido' in productNovaScore:
        return 'Nova não especificada'