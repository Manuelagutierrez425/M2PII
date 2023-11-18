import streamlit as st

#Diseño personalizado
st.header("Acerca")


def main():
    st.title('¡Robos en Transporte Público!')

    st.markdown(
        """
        <style>
        .intro-text {
            font-size: 24px;
            color: #333333;
            text-align: center;
            margin-bottom: 30px;
            font-weight: bold;
        }
        .info-text {
            font-size: 18px;
            color: #555555;
            text-align: justify;
            margin-bottom: 20px;
        }
        .warning {
            font-size: 20px;
            color: #FF5733;
            text-align: center;
            margin-top: 30px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    
    st.image("https://images.canal1.com.co/wp-content/uploads/2020/09/17163505/Urto-en-Transmilenio.jpg", width=800, caption='Robo en Transporte Público')
    st.image("https://newsweekespanol.com/wp-content/uploads/2019/07/asalto-transporte-publico-0.jpg", width=800, caption='Robo en Transporte Público')
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQABoo5xPXk3QpuqQkl092AtjLzyIYqolTBUg&usqp=CAU", width=800, caption='Robo en Transporte Público')
         
    
    st.markdown("<p class='info-text'> Los delincuentes pueden operar de diversas maneras, desde arrebatos rápidos de pertenencias hasta técnicas más elaboradas como distracciones, amenazas o forcejeos. El robo en el transporte público es una realidad preocupante en muchas ciudades. ¡No te conviertas en una estadística más! Esta aplicación te ofrece información crucial sobre easto que tanto sucede en cualquier lugar</p>", unsafe_allow_html=True)

    st.markdown("<p class='warning'>¡Tu seguridad es lo primero! Explora consejos, estadísticas y recursos para prevenir el robo en el transporte público.</p>", unsafe_allow_html=True)

    
    # Aquí podrías agregar más secciones con información relevante, imágenes, consejos, etc.

if __name__ == '__main__':
    main()
