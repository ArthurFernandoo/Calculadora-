import tkinter as tk
from tkinter import messagebox
from operacoes import Soma, Subtracao, Multiplicacao, Divisao


class CalculadoraApp:
    def __init__(self, calculadora):
        self.calculadora = calculadora

        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("350x420")

        self.criar_componentes()

    def criar_componentes(self):
        tk.Label(self.janela, text="Primeiro número:").pack(pady=5)
        self.entrada_primeiro = tk.Entry(self.janela)
        self.entrada_primeiro.pack(pady=5)

        tk.Label(self.janela, text="Segundo número:").pack(pady=5)
        self.entrada_segundo = tk.Entry(self.janela)
        self.entrada_segundo.pack(pady=5)

        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="+", width=5, command=self.somar).grid(row=0, column=0, padx=3)
        tk.Button(frame_botoes, text="-", width=5, command=self.subtrair).grid(row=0, column=1, padx=3)
        tk.Button(frame_botoes, text="*", width=5, command=self.multiplicar).grid(row=0, column=2, padx=3)
        tk.Button(frame_botoes, text="/", width=5, command=self.dividir).grid(row=0, column=3, padx=3)

        self.label_resultado = tk.Label(self.janela, text="Resultado: ")
        self.label_resultado.pack(pady=5)

        tk.Button(self.janela, text="Limpar Campos", command=self.limpar_campos).pack(pady=5)

        tk.Label(self.janela, text="Histórico:").pack(pady=5)
        self.lista_historico = tk.Listbox(self.janela, width=40, height=7)
        self.lista_historico.pack(pady=5)

        tk.Button(self.janela, text="Limpar Histórico", command=self.limpar_historico).pack(pady=5)

    def calcular(self, classe_operacao, simbolo):
        try:
            a = float(self.entrada_primeiro.get())
            b = float(self.entrada_segundo.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite valores numéricos válidos.")
            return

        try:
            operacao = classe_operacao(a, b)
            resultado = self.calculadora.calcular(operacao, simbolo)
            self.label_resultado.config(text=f"Resultado: {resultado}")
            self.atualizar_historico()
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def somar(self):
        self.calcular(Soma, "+")

    def subtrair(self):
        self.calcular(Subtracao, "-")

    def multiplicar(self):
        self.calcular(Multiplicacao, "*")

    def dividir(self):
        self.calcular(Divisao, "/")

    def atualizar_historico(self):
        self.lista_historico.delete(0, tk.END)
        for item in self.calculadora.obter_historico():
            self.lista_historico.insert(tk.END, item)

    def limpar_campos(self):
        self.entrada_primeiro.delete(0, tk.END)
        self.entrada_segundo.delete(0, tk.END)
        self.label_resultado.config(text="Resultado: ")

    def limpar_historico(self):
        self.calculadora.limpar_historico()
        self.atualizar_historico()

    def executar(self):
        self.janela.mainloop()
