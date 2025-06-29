# ⚙️ Interface en ligne de commande (VOIDRA-BOT-CLI)

Ce projet inclut une CLI modulaire avec plusieurs commandes utiles, regroupées par catégories.

---

## ▶️ Commande principale

```bash
python cli.py [MODULE] [COMMANDE] [OPTIONS]
```

---

## 📚 Table des modules CLI

| Module      | Description générale                                             |
| ----------- | ---------------------------------------------------------------- |
| `simulate`  | Simulation d'une stratégie de DCA (répartition d'investissement) |
| `variation` | Calcul de variation entre deux prix                              |
| `env`       | Gestion des clés API via un fichier `.env`                       |

---

## 🔁 simulate — Simulation de DCA (Dollar Cost Averaging)

```bash
python cli.py simulate run --balance FLOAT --prix-entree FLOAT --prix-catastrophique FLOAT --drop-percent FLOAT [--export-file fichier.json]
```

**Options obligatoires** :

- `--balance` : Montant total à investir
- `--prix-entree` : Prix d'achat initial
- `--prix-catastrophique` : Seuil bas
- `--drop-percent` : Pourcentage de baisse à chaque étape

**Option facultative** :

- `--export-file` : Chemin vers un fichier `.json` pour exporter les résultats

**Exemple** :

```bash
python cli.py simulate run --balance 1000 --prix-entree 40 --prix-catastrophique 4 --drop-percent 50 --export-file resultat.json
```

---

## 📉 variation — Calcul de variation entre deux prix

```bash
python cli.py variation run --prix-initial FLOAT --prix-final FLOAT
```

**Options** :

- `--prix-initial` : Prix de départ
- `--prix-final` : Prix final

**Exemple** :

```bash
python cli.py variation run --prix-initial 100 --prix-final 80
```

> Résultat affiché :

```
📉 Le prix a baissé de 20.00%
```

---

## 🔐 env — Gestion des clés API (via .env)

### ➕ `env add-key`

Ajoute ou met à jour les clés API d’un exchange autorisé :

```bash
python cli.py env add-key --exchange EXCHANGE --api-key VOTRE_KEY --api-secret VOTRE_SECRET
```

> Exemple :

```bash
python cli.py env add-key --exchange binance --api-key abc --api-secret xyz
```

---

### 📋 `env list`

Liste toutes les clés API enregistrées :

```bash
python cli.py env list
```

---

### 🗑️ `env remove`

Supprime les clés API d’un exchange, avec confirmation :

```bash
python cli.py env remove --exchange EXCHANGE
```

> Confirmation :

```
❗ Êtes-vous sûr de vouloir supprimer les clés API pour 'binance'? [y/N]:
```

---

## ✅ Exchanges supportés

Les plateformes actuellement prises en charge sont :

- `binance`
- `kucoin`
- `binancetestnet`

> ✏️ Tu peux les étendre dans le fichier `supported_exchanges.py`.

---
