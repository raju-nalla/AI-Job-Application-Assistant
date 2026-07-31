"""
Shared configuration instance.

This module creates a single ConfigLoader instance that
can be imported throughout the application.
"""

from .config_loader import ConfigLoader

config = ConfigLoader()