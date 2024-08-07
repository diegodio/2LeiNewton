import streamlit as st
import plotly.graph_objects as go

import random

forcas_esquerda = []
forcas_direita = []
def sortear_forca(sentido):
    if sentido == 'esquerda':
        valor = random.randint(1,20)
        forcas_esquerda.append(valor)
        return valor
    
    if sentido == 'direita':
        valor = random.randint(0,20)
        forcas_direita.append(valor)
        return valor

def criar_flecha(y, sentido, fig):
    if sentido == 'direita':
        x=8
        fig.add_trace(go.Scatter(x=[x, x+1], y=[y, y], mode='lines', line=dict(color='white', width=6), hoverinfo='none'))
        fig.add_trace(go.Scatter(x=[x+0.5, x+1, x+0.5], y=[y+0.3, y, y-0.3], mode='lines', line=dict(color='white', width=6), hoverinfo='none'))
        
        
        valor = sortear_forca('direita')

        fig.add_annotation(
        x=x+1.5,  # Ajustar posição x da anotação
        y=y,  # Ajustar posição y da anotação
        text=f"<b>{valor} N</b>",
        showarrow=False,  # Remover a seta da anotação
        font=dict(
        family="Arial",
        size=18,
        color="white",
                )  # Ajustando o tamanho da fonte para 16
        )
        
        
        
        
        
    elif sentido == 'esquerda':
        x=3
        fig.add_trace(go.Scatter(x=[x, x-1], y=[y, y], mode='lines', line=dict(color='white', width=6), hoverinfo='none'))
        fig.add_trace(go.Scatter(x=[x-0.5, x-1, x-0.5], y=[y-0.3, y, y+0.3], mode='lines', line=dict(color='white', width=6), hoverinfo='none'))

        valor = sortear_forca('esquerda')
        fig.add_annotation(
        x=x-1.5,  # Ajustar posição x da anotação
        y=y,  # Ajustar posição y da anotação
        
        text=f"<b>{valor} N</b>",
        showarrow=False,  # Remover a seta da anotação
        font=dict(
        family="Arial",
        size=18,
        color="white",
                )  # Ajustando o tamanho da fonte para 16
    )
        
        
        
        
        
def criar_quadrado():
    x_quadrado = [3, 3, 8, 8, 3, 3]  # Coordenadas x dos vértices
    y_quadrado = [3, 8, 8, 3, 3, 8]  # Coordenadas y dos vértices

    # Criando o gráfico
    fig = go.Figure(go.Scatter(x=x_quadrado, y=y_quadrado, mode='lines', line=dict(color='white', width=10)))
    
    fig.update_layout(
#     title="Quadrado Simples",
    xaxis=dict(range=[0, 11], zeroline=False),
    yaxis=dict(range=[0, 11], zeroline=False),
    width=800,  # Largura da figura em pixels
    height=800,  # Altura da figura em pixels
    
    #esconder tudo
    showlegend=False,  # Esconde a legenda
    plot_bgcolor='rgba(0,0,0,0)',  # Torna o fundo transparente
    xaxis_showticklabels=False,  # Esconde os rótulos do eixo x
    yaxis_showticklabels=False  # Esconde os rótulos do eixo y
    )
    
    return fig

def gerar_lista_booleana(tamanho):
  """Gera uma lista booleana aleatória com o tamanho especificado.
  Args:
    tamanho: O tamanho da lista booleana desejada.
  Returns:
    Uma lista booleana com valores aleatórios (True ou False).
  """

  lista_booleana = []
  for _ in range(tamanho):
    lista_booleana.append(random.choice([True, False]))
  return lista_booleana

def posicionar_flechas(fig):
    listaTF = gerar_lista_booleana(6)
    for i, j in zip(range(3,9), listaTF):
        if j:
            criar_flecha(y=i, sentido='esquerda', fig=fig) 

    listaTF = gerar_lista_booleana(6)
    for i, j in zip(range(3,9), listaTF):
        if j:
            criar_flecha(y=i, sentido='direita', fig=fig)


fig = criar_quadrado()

posicionar_flechas(fig)

# fig.show()

# st.image(fig)

# img_bytes = pio.to_image(fig, format='png')
# st.image(img_bytes, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.plotly_chart(fig, theme=None)