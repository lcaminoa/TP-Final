import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de pandas con datos de ejemplo
data = pd.DataFrame({
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
    'Grade': [85, 90, 78, 92, 88]
})

# Establecer el estilo y la paleta de colores
sns.set_style("darkgrid")
sns.set_palette("deep")

# Crear un gráfico de barras con Seaborn
barplot = sns.barplot(x='Subject', y='Grade', data=data, ci="sd")

# Añadir títulos y etiquetas
plt.title('Student Grades', fontsize=20)
plt.xlabel('Subject', fontsize=15)
plt.ylabel('Grade', fontsize=15)

# Ajustar la fuente y el tamaño de las etiquetas
barplot.set_xticklabels(barplot.get_xticklabels(), size=10)

# Mostrar el gráfico
plt.show()