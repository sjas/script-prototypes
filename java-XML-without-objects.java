public String createXml(List<MyLocation> locationList) {
    XmlSerializer serializer = Xml.newSerializer();

    StringWriter stringWriter = new StringWriter();

    try {
        serializer.setOutput(stringWriter);
        serializer.startDocument("UTF-8", true);
        serializer.startTag("", "training");
        if (locationList.size() > 0) {
            serializer.startTag("", "datetime");
            // don't know if next line is correct, due to c&p from skype
            //serializer.text(String.valueOf(locationList.getTime(0)
              serializer.text(String.valueOf(locationList.get(0)
                        .getTimeAsLong()));
            serializer.endTag("", "datetime");
        }
        for (MyLocation location : locationList) {
            serializer.startTag("", "location");
            serializer.startTag("", "longitude");
            serializer.text(String.valueOf(location.getLongitude()));
            serializer.endTag("", "longitude");
            serializer.startTag("", "latitude");
            serializer.text(String.valueOf(location.getLatitude()));
            serializer.endTag("", "latitude");
            serializer.endTag("", "location");
        }
        serializer.endTag("", "training");
        serializer.endDocument();
    } catch (IllegalArgumentException e) {
    } catch (IllegalStateException e) {
    } catch (IOException e) {
    }
    return stringWriter.toString();
}
