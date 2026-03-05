#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
knn_imputation_example.py
=========================
Ejemplo reproducible de imputación de datos faltantes
mediante K-Nearest Neighbors (KNN) usando scikit-learn.

Incluye:
  - Generación de un dataset de ejemplo
  - Introducción de valores faltantes
  - Imputación con KNNImputer
  - Comparación visual de resultados

Dependencias:
  - numpy
  - pandas
  - matplotlib
  - scikit-learn

Autor: Guillermo · ICTA Ltda.
Fecha: 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
import os

# ──────────────────────────────────────────────
# Configuración
# ──────────────────────────────────────────────
SEED = 42
N = 200
K_NEIGHBORS = 5
FRAC_MISSING = 0.15

FIGURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

np.random.seed(SEED)

# ──────────────────────────────────────────────
# 1. Generar dataset de ejemplo multivariado
# ──────────────────────────────────────────────
# Variables correlacionadas: temperatura, humedad, precipitación
temperature = np.random.normal(loc=22, scale=5, size=N)
humidity = 60 + 0.8 * temperature + np.random.normal(0, 3, size=N)
precipitation = 10 + 0.5 * humidity - 0.3 * temperature + np.random.normal(0, 2, size=N)

df_original = pd.DataFrame({
    'temperatura': temperature,
    'humedad': humidity,
    'precipitacion': precipitation
})

print("=== Dataset Original ===")
print(df_original.describe().round(2))

# Guardar dataset original
df_original.to_csv(os.path.join(DATA_DIR, 'sample_dataset.csv'), index=False)
print(f"\nDataset guardado en: {os.path.join(DATA_DIR, 'sample_dataset.csv')}")

# ──────────────────────────────────────────────
# 2. Introducir valores faltantes
# ──────────────────────────────────────────────
df_missing = df_original.copy()

for col in df_missing.columns:
    missing_idx = df_missing.sample(frac=FRAC_MISSING, random_state=SEED).index
    df_missing.loc[missing_idx, col] = np.nan

n_missing_total = df_missing.isna().sum().sum()
print(f"\nValores faltantes introducidos: {n_missing_total}")
print(f"Valores faltantes por columna:")
print(df_missing.isna().sum())

# ──────────────────────────────────────────────
# 3. Imputación con KNN
# ──────────────────────────────────────────────
imputer = KNNImputer(n_neighbors=K_NEIGHBORS, weights='uniform')
df_knn_imputed = pd.DataFrame(
    imputer.fit_transform(df_missing),
    columns=df_missing.columns
)

print(f"\n=== Dataset Imputado con KNN (K={K_NEIGHBORS}) ===")
print(df_knn_imputed.describe().round(2))

# ──────────────────────────────────────────────
# 4. Imputación con Media (para comparación)
# ──────────────────────────────────────────────
df_mean_imputed = df_missing.fillna(df_missing.mean())

# ──────────────────────────────────────────────
# 5. Comparación de estadísticas
# ──────────────────────────────────────────────
print("\n=== Comparación de Estadísticas ===")
for col in df_original.columns:
    print(f"\n--- {col} ---")
    print(f"  {'Métrica':<15} {'Original':>10} {'Media':>10} {'KNN':>10}")
    print(f"  {'-'*50}")
    print(f"  {'Media':<15} {df_original[col].mean():>10.2f} {df_mean_imputed[col].mean():>10.2f} {df_knn_imputed[col].mean():>10.2f}")
    print(f"  {'Desv. Est.':<15} {df_original[col].std():>10.2f} {df_mean_imputed[col].std():>10.2f} {df_knn_imputed[col].std():>10.2f}")
    print(f"  {'Varianza':<15} {df_original[col].var():>10.2f} {df_mean_imputed[col].var():>10.2f} {df_knn_imputed[col].var():>10.2f}")

# ──────────────────────────────────────────────
# 6. Visualización comparativa
# ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

for i, col in enumerate(df_original.columns):
    ax = axes[i]
    ax.hist(df_original[col], bins=20, alpha=0.5, color='#4C72B0', label='Original', edgecolor='white')
    ax.hist(df_mean_imputed[col], bins=20, alpha=0.4, color='#DD8452', label='Imputación Media', edgecolor='white')
    ax.hist(df_knn_imputed[col], bins=20, alpha=0.4, color='#55A868', label='Imputación KNN', edgecolor='white')
    ax.set_title(f'{col.capitalize()}', fontsize=13, fontweight='bold')
    ax.set_xlabel('Valor', fontsize=11)
    ax.set_ylabel('Frecuencia', fontsize=11)
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.suptitle('Comparación: Distribución Original vs. Imputación por Media vs. Imputación KNN',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()

output_path = os.path.join(FIGURES_DIR, 'knn_vs_mean_comparison.png')
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"\nFigura guardada en: {output_path}")
plt.close()

# ──────────────────────────────────────────────
# 7. Scatter plot: Original vs. Imputado
# ──────────────────────────────────────────────
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))

# Scatter: temperatura vs humedad
axes2[0].scatter(df_original['temperatura'], df_original['humedad'],
                 alpha=0.4, color='#4C72B0', label='Original', s=30)
axes2[0].scatter(df_knn_imputed['temperatura'], df_knn_imputed['humedad'],
                 alpha=0.4, color='#55A868', label='KNN Imputado', s=30, marker='x')
axes2[0].set_xlabel('Temperatura (°C)', fontsize=11)
axes2[0].set_ylabel('Humedad (%)', fontsize=11)
axes2[0].set_title('Temperatura vs. Humedad', fontsize=13, fontweight='bold')
axes2[0].legend(fontsize=9)
axes2[0].spines['top'].set_visible(False)
axes2[0].spines['right'].set_visible(False)

# Scatter: humedad vs precipitación
axes2[1].scatter(df_original['humedad'], df_original['precipitacion'],
                 alpha=0.4, color='#4C72B0', label='Original', s=30)
axes2[1].scatter(df_knn_imputed['humedad'], df_knn_imputed['precipitacion'],
                 alpha=0.4, color='#55A868', label='KNN Imputado', s=30, marker='x')
axes2[1].set_xlabel('Humedad (%)', fontsize=11)
axes2[1].set_ylabel('Precipitación (mm)', fontsize=11)
axes2[1].set_title('Humedad vs. Precipitación', fontsize=13, fontweight='bold')
axes2[1].legend(fontsize=9)
axes2[1].spines['top'].set_visible(False)
axes2[1].spines['right'].set_visible(False)

plt.suptitle('Relaciones entre Variables: Original vs. Imputación KNN',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()

output_path2 = os.path.join(FIGURES_DIR, 'knn_scatter_comparison.png')
fig2.savefig(output_path2, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Figura guardada en: {output_path2}")
plt.close()

print("\n✓ Todas las figuras y datos generados exitosamente.")
