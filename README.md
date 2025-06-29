# voidra-bot-cli

CLI avec une architecture modulaire.

---

## ✅ Strcture :

- Placer les script dans `scripts/`
- Créer une commande CLI dans `commands/` qui l’utilise
- Rajouté l'appel dans le point d’entrée principal

---

## ✅ Utilisation dans le terminal `simulation_calcule.py`

```bash
python cli.py simulate run \
  --balance 1000 \
  --prix-entree 40 \
  --prix-catastrophique 4 \
  --drop-percent 50 \
  --export-file resultat.json
```

Ou sans export :

```bash
python cli.py simulate run --balance 1000 --prix-entree 40 --prix-catastrophique 4 --drop-percent 50
```

---
