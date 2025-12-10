# The Golden Pipeline Project

Goal: Create a secure CI/CD pipeline that detects vulnerabilities before deployment.

Tools Used:

- GitHub Actions: CI/CD Orchestration

- Bandit: SAST (Static Application Security Testing) for Python

- Trivy: SCA (Software Composition Analysis) and Container Scanning

- Docker: Containerization


How it works:

- Developer pushes code.

- Bandit scans source code for secrets/bad patterns.

- Trivy scans requirements.txt for known CVEs.

- Docker image is built.

- Trivy scans the final image for OS vulnerabilities.