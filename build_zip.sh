#!/bin/bash
set -e
echo "📦 Generando isekai_races_v0.1.zip (datapack)..."

# Preferimos usar curseforge/overrides/datapacks/isekai si existe, si no, datapack/isekai
if [ -d "curseforge/overrides/datapacks/isekai" ]; then
  SRC="curseforge/overrides/datapacks/isekai"
elif [ -d "datapack/isekai" ]; then
  SRC="datapack/isekai"
else
  echo "❌ No se encontró datapack en curseforge/overrides/datapacks/isekai ni en datapack/isekai"
  exit 1
fi

echo "Usando fuente: $SRC"

if [ ! -f "$SRC/pack.mcmeta" ] || [ ! -d "$SRC/data" ]; then
  echo "❌ pack.mcmeta o data/ no encontrado en $SRC"
  exit 1
fi

# Crear ZIP en la raíz del repo
OUT="../../isekai_races_v0.1.zip"
if [ "$SRC" = "datapack/isekai" ]; then
  OUT="../isekai_races_v0.1.zip"
fi

# Asegurar ruta absoluta para evitar problemas con pushd/popd
pushd "$SRC" > /dev/null
zip -r "$OUT" pack.mcmeta data
popd > /dev/null

echo "✓ isekai_races_v0.1.zip creado: $OUT"
