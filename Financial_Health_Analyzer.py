{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPIHjoslDbUQWtbx8I6Qaxi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Andradeus/Project-Financial-Health-Analyzer/blob/main/Financial_Health_Analyzer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "De-ABbmdZAqb",
        "outputId": "400a01c1-4695-4c95-f39b-556e3c881c09"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Analisando Saúde Financeira da Apple...\n",
            "--- Relatório de Análise ---\n",
            "Current Ratio: 0.89 (CFA diz: > 1.0 é saudável)\n",
            "Net Profit Margin: 26.92%\n",
            "ROE: 151.91%\n",
            "Veredito: Atenção necessária na Liquidez.\n"
          ]
        }
      ],
      "source": [
        "import yfinance as ticker_data\n",
        "\n",
        "#This project uses the yfinance library to analyze Apple's liquidity and profitability ratios, based on the CFA Level 1 syllabus\n",
        "\n",
        "# 1. Definir a empresa (Exemplo: Apple - AAPL)\n",
        "empresa = ticker_data.Ticker(\"AAPL\")\n",
        "print(\"Analisando Saúde Financeira da Apple...\")\n",
        "\n",
        "# 2. Balanço Patrimonial e a DRE\n",
        "balanco = empresa.balance_sheet\n",
        "dre = empresa.financials\n",
        "\n",
        "# 3. Extrair termos técnicos (Usando dados do último ano)\n",
        "current_assets = balanco.loc['Current Assets'].iloc[0]\n",
        "current_liabilities = balanco.loc['Current Liabilities'].iloc[0]\n",
        "net_income = dre.loc['Net Income'].iloc[0]\n",
        "revenue = dre.loc['Total Revenue'].iloc[0]\n",
        "\n",
        "# 4. Cálculos de Investment Banking\n",
        "current_ratio = current_assets / current_liabilities  # Liquidez Corrente\n",
        "net_profit_margin = (net_income / revenue) * 100      # Margem de Lucro Líquida\n",
        "\n",
        "# 5. Output\n",
        "print(f\"--- Relatório de Análise ---\")\n",
        "print(f\"Current Ratio: {current_ratio:.2f} (CFA diz: > 1.0 é saudável)\")\n",
        "print(f\"Net Profit Margin: {net_profit_margin:.2f}%\")\n",
        "\n",
        "#6 Calculando ROE:\n",
        "equity = balanco.loc['Stockholders Equity'].iloc[0]\n",
        "roe = (net_income / equity) * 100\n",
        "print(f\"ROE: {roe:.2f}%\")\n",
        "\n",
        "if current_ratio > 1.5:\n",
        "    print(\"Veredito: Forte Liquidez de Curto Prazo.\")\n",
        "else:\n",
        "    print(\"Veredito: Atenção necessária na Liquidez.\")"
      ]
    }
  ]
}