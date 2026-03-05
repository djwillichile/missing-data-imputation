#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_histograms.py
======================
Script para generar tres histogramas que ilustran el problema
de la imputación por media en datos faltantes.

Histogramas generados:
  1. Distribución original (normal simulada)
  2. Distribución con valores eliminados (listwise deletion)
  3. Distribución con imputación por media

Dependencias:
  - numpy
  - pandas
  - matplotlib

Autor: Guillermo · ICTA Ltda.
Fecha: 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ──────────────────────────────────────────────
# Configuración
# ──────────────────────────────────────────────
SEED = 42
N = 1000
MEAN = 170          # Media de la distribución (ej. altura en cm)
STD = 10            # Desviación estándar
FRAC_MISSING = 0.30 # Proporción de datos faltantes

FIGURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

# ──────────────────────────────────────────────
# 1. Generar datos originales
# ──────────────────────────────────────────────
np.random.seed(SEED)
original_data = np.random.normal(loc=MEAN, scale=STD, size=N)

# ──────────────────────────────────────────────
# 2. Introducir valores faltantes (MCAR)
# ──────────────────────────────────────────────
data_series = pd.Series(original_data.copy())
missing_indices = data_series.sample(frac=FRAC_MISSING, random_state=SEED).index
data_with_missing = data_series.copy()
data_with_missing.iloc[missing_indices] = np.nan

n_missing = data_with_missing.isna().sum()
print(f"Total de observaciones: {N}")
print(f"Valores faltantes introducidos: {n_missing} ({n_missing/N*100:.1f}%)")

# ──────────────────────────────────────────────
# 3. Datos con eliminación (listwise deletion)
# ──────────────────────────────────────────────
data_deleted = data_with_missing.dropna()
print(f"Observaciones después de eliminación: {len(data_deleted)}")

# ──────────────────────────────────────────────
# 4. Datos con imputación por media
# ──────────────────────────────────────────────
imputed_mean = data_with_missing.mean()
data_mean_imputed = data_with_missing.fillna(imputed_mean)
print(f"Media utilizada para imputación: {imputed_mean:.2f}")

# ──────────────────────────────────────────────
# 5. Estadísticas comparativas
# ──────────────────────────────────────────────
print("\n--- Estadísticas Comparativas ---")
print(f"{'Métrica':<20} {'Original':>12} {'Eliminación':>12} {'Imputación':>12}")
print("-" * 60)
print(f"{'N':.<20} {len(original_data):>12} {len(data_deleted):>12} {len(data_mean_imputed):>12}")
print(f"{'Media':.<20} {original_data.mean():>12.2f} {data_deleted.mean():>12.2f} {data_mean_imputed.mean():>12.2f}")
print(f"{'Desv. Estándar':.<20} {original_data.std():>12.2f} {data_deleted.std():>12.2f} {data_mean_imputed.std():>12.2f}")
print(f"{'Varianza':.<20} {original_data.var():>12.2f} {data_deleted.var():>12.2f} {data_mean_imputed.var():>12.2f}")

# ──────────────────────────────────────────────
# 6. Generar histogramas
# ──────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), sharex=True, sharey=True)

# Estilo general
for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Histograma 1: Datos originales
axes[0].hist(original_data, bins=30, color='#4C72B0', edgecolor='white', alpha=0.85)
axes[0].set_title('1. Distribución Original\n(n = 1000)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Valor (altura en cm)', fontsize=11)
axes[0].set_ylabel('Frecuencia', fontsize=11)
axes[0].axvline(original_data.mean(), color='#C44E52', linestyle='--', linewidth=1.5,
                label=f'Media: {original_data.mean():.2f}')
axes[0].legend(fontsize=9)

# Histograma 2: Datos con eliminación
axes[1].hist(data_deleted, bins=30, color='#DD8452', edgecolor='white', alpha=0.85)
axes[1].set_title(f'2. Distribución con Eliminación\n(n = {len(data_deleted)})', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Valor (altura en cm)', fontsize=11)
axes[1].axvline(data_deleted.mean(), color='#C44E52', linestyle='--', linewidth=1.5,
                label=f'Media: {data_deleted.mean():.2f}')
axes[1].legend(fontsize=9)

# Histograma 3: Datos con imputación por media
axes[2].hist(data_mean_imputed, bins=30, color='#55A868', edgecolor='white', alpha=0.85)
axes[2].set_title(f'3. Distribución con Imputación por Media\n(n = {len(data_mean_imputed)})', fontsize=13, fontweight='bold')
axes[2].set_xlabel('Valor (altura en cm)', fontsize=11)
axes[2].axvline(imputed_mean, color='#C44E52', linestyle='--', linewidth=2,
                label=f'Media Imputada: {imputed_mean:.2f}')
axes[2].legend(fontsize=9)

plt.suptitle('Comparación de Distribuciones: Efecto de la Imputación por Media',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()

output_path = os.path.join(FIGURES_DIR, 'imputation_comparison.png')
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"\nFigura guardada en: {output_path}")
plt.close()

# ──────────────────────────────────────────────
# 7. Generar histograma de comparación de varianza
# ──────────────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(8, 5))

variances = [original_data.var(), data_deleted.var(), data_mean_imputed.var()]
labels = ['Original', 'Eliminación', 'Imputación\npor Media']
colors = ['#4C72B0', '#DD8452', '#55A868']

bars = ax2.bar(labels, variances, color=colors, edgecolor='white', width=0.6)
ax2.set_title('Comparación de Varianza entre Métodos', fontsize=14, fontweight='bold')
ax2.set_ylabel('Varianza', fontsize=12)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

for bar, var in zip(bars, variances):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{var:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

output_path2 = os.path.join(FIGURES_DIR, 'variance_comparison.png')
fig2.savefig(output_path2, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Figura guardada en: {output_path2}")
plt.close()

print("\n✓ Todas las figuras generadas exitosamente.")
