# 🤖 Projeto FLL - Base Pybricks

Este repositório contém uma estrutura de projeto em **Python (Pybricks)** para equipes da **FIRST LEGO League (FLL)**.  
A ideia é servir de **base** para criação, organização e manutenção de programas do robô, facilitando a colaboração da equipe.

---

## 📂 Estrutura do Projeto

```
├── Anexo.py      # Código relacionado ao uso de anexos/mecanismos adicionais
├── Chassi.py     # Funções principais de movimentação do robô (chassi/base)
├── MissaoA.py    # Estratégia e programação da Missão A
├── MissaoB.py    # Estratégia e programação da Missão B
├── MissaoC.py    # Estratégia e programação da Missão C
└── menu.py       # Ponto de entrada do programa (seleção de missões)
```

Essa organização permite separar cada parte do robô em **módulos independentes**, tornando o código mais limpo e fácil de reutilizar.

---

# 🔋 Nível de Bateria

A cor do indicador representa o nível atual da bateria com base na voltagem medida:

| Cor         | Nível da Bateria | Faixa de Voltagem         |
|-------------|------------------|----------------------------|
| 🟢 Verde    | Bateria Cheia    | Maior que 8200 mV          |
| 🟡 Amarelo  | Bateria Média    | Entre 7500 mV e 8200 mV    |
| 🔴 Vermelho | Bateria Fraca    | Menor que 7500 mV          |

---

## 🛠️ Personalização

- Crie novos arquivos para cada missão: `MissaoD.py`, `MissaoE.py`, etc.  
- Adicione funções no `Chassi.py` para novas movimentações do robô.  
- Atualize `menu.py` para incluir novas opções de missões.

---

## 👥 Contribuindo

Este projeto foi feito para ajudar a equipe FLL a **trabalhar em conjunto**.  
Sugestões de melhorias e novas ideias são bem-vindas!

