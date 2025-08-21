.PHONY: venv install run lint clean

# Windows users: run this in PowerShell via 'make' from MSYS/WSL or use the equivalent commands shown in README.
PYTHON := python
VENV_DIR := .venv

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "虚拟环境已创建：$(VENV_DIR)"

install: venv
	$(VENV_DIR)\Scripts\pip install --upgrade pip
	$(VENV_DIR)\Scripts\pip install -r requirements.txt
	@echo "依赖已安装。"

run:
	$(VENV_DIR)\Scripts\python main.py --both

lint:
	@echo "暂未配置 lint。可手动运行 flake8 或 pylint。"

clean:
	rm -rf $(VENV_DIR)
	@echo "已清理虚拟环境。"
