PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set -euo pipefail

export COMPOSE_FILE=${PROJECT_DIR}/docker-compose.yaml
exec docker-compose run airflow-worker "${@}"