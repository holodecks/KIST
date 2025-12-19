#!/usr/bin/env python
"""venv環境の診断スクリプト"""
import sys
import subprocess

print("=" * 60)
print("Python環境診断")
print("=" * 60)
print(f"Python実行パス: {sys.executable}")
print(f"Pythonバージョン: {sys.version}")
print()

print("=" * 60)
print("インストール済みパッケージ (streamlit関連)")
print("=" * 60)
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list"],
        capture_output=True,
        text=True
    )
    for line in result.stdout.split("\n"):
        if any(keyword in line.lower() for keyword in ["streamlit", "gsheet", "pandas"]):
            print(line)
except Exception as e:
    print(f"エラー: {e}")

print()
print("=" * 60)
print("st-gsheets-connection の詳細情報")
print("=" * 60)
try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "show", "st-gsheets-connection"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
except Exception as e:
    print(f"エラー: {e}")

print()
print("=" * 60)
print("インポートテスト")
print("=" * 60)

# Test 1: streamlit_gsheets
try:
    from streamlit_gsheets import GSheetsConnection
    print("✓ from streamlit_gsheets import GSheetsConnection - 成功")
except ImportError as e:
    print(f"✗ from streamlit_gsheets import GSheetsConnection - 失敗: {e}")

# Test 2: st_gsheets_connection (アンダースコア版)
try:
    import st_gsheets_connection
    print(f"✓ import st_gsheets_connection - 成功")
    print(f"  利用可能な属性: {dir(st_gsheets_connection)}")
except ImportError as e:
    print(f"✗ import st_gsheets_connection - 失敗: {e}")

print()
print("=" * 60)
print("診断完了")
print("=" * 60)
