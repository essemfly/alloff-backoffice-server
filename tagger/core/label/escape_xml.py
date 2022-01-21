def escape_xml(xml):
    xml = xml.replace("&", "&amp;")
    xml = xml.replace("<", "&lt;")
    xml = xml.replace(">", "&gt;")
    xml = xml.replace("\"", "&quot;")
    return xml
