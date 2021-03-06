#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of the Wapiti project (https://wapiti.sourceforge.io)
# Copyright (C) 2021 Nicolas Surribas
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
from wapitiCore.language.language import _

TYPE = "additional"

NAME = _("HTTP Secure Headers")
SHORT_NAME = NAME

DESCRIPTION = _(
    "HTTP security headers tell the browser how to behave when handling the website's content."
)

SOLUTION = _(
    "Use the recommendations for hardening your HTTP Security Headers."
)

REFERENCES = [
    {
        "title": "Netsparker: HTTP Security Headers: An Easy Way to Harden Your Web Applications",
        "url": "https://www.netsparker.com/blog/web-security/http-security-headers/"
    },
    {
        "title": "KeyCDN: Hardening Your HTTP Security Headers",
        "url": "https://www.keycdn.com/blog/http-security-headers"
    },
    {
        "title": "OWASP: HTTP SECURITY HEADERS (Protection For Browsers) (PDF)",
        "url": "https://owasp.org/www-chapter-ghana/assets/slides/HTTP_Header_Security.pdf"
    }
]
