"""Regresión de integración externa Brevo sin peticiones de red ni datos reales."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://4f9dfb6b.sibforms.com/serve/MUIFAOEVJOWAlKsARg_U77j090I8bkCuEuA97CEvQ-ExPFJN27WIB1WasOqKCOLGMdVuN6G9m8YnzmRs7Unu04sH9Dma355G6d8KZNUG6hDaRSW5gP919--vqB-dFAblnsa3TLO-qOuNmQ9DxCf8tGvHVIzWe6GD4MhFRWmpRS-miivXtbCTGpa6OBKvRSkXv8Vn3xanDnjCK0bgcg=="

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "a":
            self.anchors.append(dict(attrs))

class BrevoLinks(unittest.TestCase):
    def test_enlaces_autenticos_e_identicos(self):
        for page in ("index.html", "kit.html"):
            with self.subTest(page=page):
                html = (ROOT / page).read_text(encoding="utf8")
                parser = Anchors()
                parser.feed(html)
                brevo = [a for a in parser.anchors if "sibforms.com" in a.get("href", "")]
                self.assertEqual(len(brevo), 1)
                self.assertEqual(brevo[0]["href"], URL)
                self.assertEqual(brevo[0].get("target"), "_blank")
                self.assertTrue({"noopener", "noreferrer"}.issubset(set(brevo[0].get("rel", "").split())))
                self.assertNotIn('mailto:pixelredmedia@gmail.com?subject=Alta', html)
                self.assertNotIn("script", parser.tags)
                self.assertNotIn("iframe", parser.tags)
                self.assertIn("form-action 'none'", html)
                self.assertIn('href="privacidad.html"', html)

    def test_pdf_gratis_sin_registro(self):
        html = (ROOT / "kit.html").read_text(encoding="utf8")
        self.assertTrue((ROOT / "recursos" / "kit-agente-en-practicas.pdf").exists())
        self.assertIn('href="recursos/kit-agente-en-practicas.pdf" download', html)
        self.assertIn("sin dar tu correo ni suscribirte", html.lower())

    def test_informacion_privacidad_proveedor(self):
        html = (ROOT / "privacidad.html").read_text(encoding="utf8")
        self.assertIn("Brevo", html)
        self.assertIn("Gmail", html)
        self.assertIn("pixelredmedia@gmail.com", html)
        self.assertIn("consentimiento expreso", html)
        self.assertIn("8 de noviembre de 2026", html)

if __name__ == "__main__":
    unittest.main()
