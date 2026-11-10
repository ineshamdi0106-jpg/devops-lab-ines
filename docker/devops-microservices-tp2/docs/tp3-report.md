# TP3 – Docker Networking & Compose

## 1. Exploration réseau
| Réseau | Driver | Subnet | Gateway |
|---|---|---|---|
| bridge (défaut) | bridge | 172.17.0.0/16 | 172.17.0.1 |
| tp3-net (utilisateur) | bridge | 172.20.0.0/16 | 172.20.0.1 |

nslookup tp3-web depuis tp3-net : 172.20.0.2 (DNS interne 127.0.0.11).

## 2. Déploiement Compose
Réseau : devops-microservices-tp2_app-net. Product : 172.20.0.2, Order : 172.20.0.3.

## 3. Tests API
- GET :8001/products : Laptop (1200), Mouse (25)
- GET :8001/health et :8002/health : status running
- POST :8002/orders (product 1, qty 2) : total 2400
- DNS : product-service résolu en 172.20.0.2

## 4. Panne et reprise
- Product arrêté : POST /orders renvoie 500 (NameResolutionError: Failed to resolve 'product-service'), Order reste Up.
- Après start : POST /orders renvoie 201 (Mouse, total 25).

## 5. Limites et adaptations
- Port de Product passé de 5000 à 8001 dans app.py.
- Route /health ajoutée à Product Service.
- Dockerfile.reference créés (COPY adaptés au contexte racine).
- La réponse du POST contient order_id et non product_id.
- Order renvoie 500 si Product est indisponible (502/503 plus adapté).

## 6. Réponses Q1 à Q8
(à compléter)
