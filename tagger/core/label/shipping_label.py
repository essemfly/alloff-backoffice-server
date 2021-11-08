from tagger.core.mongo.models.order import Order


def make_shipping_label(order: Order) -> str:
    payment = order.get_payment()
    return _get_shipping_label_xml(
        f"""{payment.buyername.replace("<", "(").replace(">", ")")} ({payment.buyermobile})""",
        payment.name,
        order.code.replace("ORD-", ""),
        f"https://office.alloff.co/orders/{order.id}",
        payment.buyeraddress,
        ",".join([x.size for x in order.orders]),
        order.memo
    )


def _get_shipping_label_xml(name_mobile: str, order_name: str, order_code: str, url: str, address: str, size: str,
                            order_memo: str):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<DesktopLabel Version="1">
  <DYMOLabel Version="3">
    <Description>DYMO Label</Description>
    <Orientation>Landscape</Orientation>
    <LabelName>Addresss0722370</LabelName>
    <InitialLength>0</InitialLength>
    <BorderStyle>SolidLine</BorderStyle>
    <DYMORect>
      <DYMOPoint>
        <X>0.23</X>
        <Y>0.06</Y>
      </DYMOPoint>
      <Size>
        <Width>3.21</Width>
        <Height>0.9966666</Height>
      </Size>
    </DYMORect>
    <BorderColor>
      <SolidColorBrush>
        <Color A="1" R="0" G="0" B="0"></Color>
      </SolidColorBrush>
    </BorderColor>
    <BorderThickness>1</BorderThickness>
    <Show_Border>False</Show_Border>
    <DynamicLayoutManager>
      <RotationBehavior>ClearObjects</RotationBehavior>
      <LabelObjects>
        <QRCodeObject>
          <Name>QR</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="1" R="1" G="1" B="1"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <BarcodeFormat>QRCode</BarcodeFormat>
          <Data>
            <DataString>{url}</DataString>
          </Data>
          <HorizontalAlignment>Center</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <Size>Medium</Size>
          <EQRCodeType>QRCodeText</EQRCodeType>
          <TextDataHolder>
            <Value>{url}</Value>
          </TextDataHolder>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.23</X>
              <Y>0.1250747</Y>
            </DYMOPoint>
            <Size>
              <Width>0.6269797</Width>
              <Height>0.6374313</Height>
            </Size>
          </ObjectLayout>
        </QRCodeObject>
        <TextObject>
          <Name>ProductTypeId</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Left</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Left</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{address}</Text>
                <FontInfo>
                  <FontName>Noto Sans KR</FontName>
                  <FontSize>8</FontSize>
                  <IsBold>True</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.8616675</X>
              <Y>0.6977562</Y>
            </DYMOPoint>
            <Size>
              <Width>2.578332</Width>
              <Height>0.2095642</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
        <TextObject>
          <Name>BrandKeyname4</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Left</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Left</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{size}</Text>
                <FontInfo>
                  <FontName>Noto Sans KR</FontName>
                  <FontSize>8</FontSize>
                  <IsBold>False</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.8616673</X>
              <Y>0.545</Y>
            </DYMOPoint>
            <Size>
              <Width>2.578333</Width>
              <Height>0.171832</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
        <ImageObject>
          <Name>IImageObject0</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <Data>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</Data>
          <ScaleMode>Uniform</ScaleMode>
          <HorizontalAlignment>Center</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <ObjectLayout>
            <DYMOPoint>
              <X>3.081481</X>
              <Y>0.07000001</Y>
            </DYMOPoint>
            <Size>
              <Width>0.3385193</Width>
              <Height>0.3191779</Height>
            </Size>
          </ObjectLayout>
        </ImageObject>
        <TextObject>
          <Name>InventoryCode3</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Center</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Center</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{order_code}</Text>
                <FontInfo>
                  <FontName>Hack</FontName>
                  <FontSize>12</FontSize>
                  <IsBold>True</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.23</X>
              <Y>0.7625059</Y>
            </DYMOPoint>
            <Size>
              <Width>0.6109899</Width>
              <Height>0.289629</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
        <TextObject>
          <Name>ProductTypeId4</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Left</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Left</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{name_mobile}</Text>
                <FontInfo>
                  <FontName>Noto Sans KR</FontName>
                  <FontSize>12</FontSize>
                  <IsBold>True</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.8616674</X>
              <Y>0.0603249</Y>
            </DYMOPoint>
            <Size>
              <Width>2.190481</Width>
              <Height>0.289629</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
        <TextObject>
          <Name>ProductTypeId5</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Left</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Left</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{order_name}</Text>
                <FontInfo>
                  <FontName>Noto Sans KR</FontName>
                  <FontSize>8</FontSize>
                  <IsBold>False</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.8616674</X>
              <Y>0.3499539</Y>
            </DYMOPoint>
            <Size>
              <Width>2.578333</Width>
              <Height>0.2095642</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
        <TextObject>
          <Name>ProductTypeId6</Name>
          <Brushes>
            <BackgroundBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BackgroundBrush>
            <BorderBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </BorderBrush>
            <StrokeBrush>
              <SolidColorBrush>
                <Color A="1" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </StrokeBrush>
            <FillBrush>
              <SolidColorBrush>
                <Color A="0" R="0" G="0" B="0"></Color>
              </SolidColorBrush>
            </FillBrush>
          </Brushes>
          <Rotation>Rotation0</Rotation>
          <OutlineThickness>1</OutlineThickness>
          <IsOutlined>False</IsOutlined>
          <BorderStyle>SolidLine</BorderStyle>
          <Margin>
            <DYMOThickness Left="0" Top="0" Right="0" Bottom="0" />
          </Margin>
          <HorizontalAlignment>Left</HorizontalAlignment>
          <VerticalAlignment>Middle</VerticalAlignment>
          <FitMode>None</FitMode>
          <IsVertical>False</IsVertical>
          <FormattedText>
            <FitMode>None</FitMode>
            <HorizontalAlignment>Left</HorizontalAlignment>
            <VerticalAlignment>Middle</VerticalAlignment>
            <IsVertical>False</IsVertical>
            <LineTextSpan>
              <TextSpan>
                <Text>{order_memo}</Text>
                <FontInfo>
                  <FontName>Noto Sans KR</FontName>
                  <FontSize>8</FontSize>
                  <IsBold>False</IsBold>
                  <IsItalic>False</IsItalic>
                  <IsUnderline>False</IsUnderline>
                  <FontBrush>
                    <SolidColorBrush>
                      <Color A="1" R="0" G="0" B="0"></Color>
                    </SolidColorBrush>
                  </FontBrush>
                </FontInfo>
              </TextSpan>
            </LineTextSpan>
          </FormattedText>
          <ObjectLayout>
            <DYMOPoint>
              <X>0.8616682</X>
              <Y>0.8593361</Y>
            </DYMOPoint>
            <Size>
              <Width>2.578332</Width>
              <Height>0.2095642</Height>
            </Size>
          </ObjectLayout>
        </TextObject>
      </LabelObjects>
    </DynamicLayoutManager>
  </DYMOLabel>
  <LabelApplication>Blank</LabelApplication>
  <DataTable>
    <Columns></Columns>
    <Rows></Rows>
  </DataTable>
</DesktopLabel>"""
