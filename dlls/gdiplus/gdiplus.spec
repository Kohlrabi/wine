@ stdcall GdipAddPathArc(ptr long long long long long long)
@ stub GdipAddPathArcI
@ stub GdipAddPathBezier
@ stdcall GdipAddPathBezierI(ptr long long long long long long long long)
@ stdcall GdipAddPathBeziers(ptr ptr long)
@ stub GdipAddPathBeziersI
@ stub GdipAddPathClosedCurve2
@ stub GdipAddPathClosedCurve2I
@ stub GdipAddPathClosedCurve
@ stub GdipAddPathClosedCurveI
@ stub GdipAddPathCurve2
@ stub GdipAddPathCurve2I
@ stub GdipAddPathCurve3
@ stub GdipAddPathCurve3I
@ stub GdipAddPathCurve
@ stub GdipAddPathCurveI
@ stdcall GdipAddPathEllipse(ptr long long long long)
@ stub GdipAddPathEllipseI
@ stdcall GdipAddPathLine2(ptr ptr long)
@ stub GdipAddPathLine2I
@ stub GdipAddPathLine
@ stdcall GdipAddPathLineI(ptr long long long long)
@ stdcall GdipAddPathPath(ptr ptr long)
@ stub GdipAddPathPie
@ stub GdipAddPathPieI
@ stub GdipAddPathPolygon
@ stub GdipAddPathPolygonI
@ stub GdipAddPathRectangle
@ stub GdipAddPathRectangleI
@ stub GdipAddPathRectangles
@ stub GdipAddPathRectanglesI
@ stub GdipAddPathString
@ stub GdipAddPathStringI
@ stdcall GdipAlloc(long)
@ stub GdipBeginContainer2
@ stub GdipBeginContainer
@ stub GdipBeginContainerI
@ stub GdipBitmapApplyEffect
@ stub GdipBitmapConvertFormat
@ stub GdipBitmapCreateApplyEffect
@ stub GdipBitmapGetHistogram
@ stub GdipBitmapGetHistogramSize
@ stdcall GdipBitmapGetPixel(ptr long long ptr)
@ stdcall GdipBitmapLockBits(ptr ptr long long ptr)
@ stub GdipBitmapSetPixel
@ stub GdipBitmapSetResolution
@ stdcall GdipBitmapUnlockBits(ptr ptr)
@ stub GdipClearPathMarkers
@ stub GdipCloneBitmapArea
@ stub GdipCloneBitmapAreaI
@ stdcall GdipCloneBrush(ptr ptr)
@ stdcall GdipCloneCustomLineCap(ptr ptr)
@ stub GdipCloneFont
@ stub GdipCloneFontFamily
@ stub GdipCloneImage
@ stub GdipCloneImageAttributes
@ stdcall GdipCloneMatrix(ptr ptr)
@ stdcall GdipClonePath(ptr ptr)
@ stdcall GdipClonePen(ptr ptr)
@ stub GdipCloneRegion
@ stub GdipCloneStringFormat
@ stdcall GdipClosePathFigure(ptr)
@ stdcall GdipClosePathFigures(ptr)
@ stub GdipCombineRegionPath
@ stub GdipCombineRegionRect
@ stub GdipCombineRegionRectI
@ stub GdipCombineRegionRegion
@ stub GdipComment
@ stdcall GdipConvertToEmfPlus(ptr ptr ptr long ptr ptr)
@ stub GdipConvertToEmfPlusToFile
@ stub GdipConvertToEmfPlusToStream
@ stub GdipCreateAdjustableArrowCap
@ stub GdipCreateBitmapFromDirectDrawSurface
@ stdcall GdipCreateBitmapFromFile(wstr ptr)
@ stdcall GdipCreateBitmapFromFileICM(wstr ptr)
@ stub GdipCreateBitmapFromGdiDib
@ stdcall GdipCreateBitmapFromGraphics(long long ptr ptr)
@ stdcall GdipCreateBitmapFromHBITMAP(ptr ptr ptr)
@ stub GdipCreateBitmapFromHICON
@ stub GdipCreateBitmapFromResource
@ stdcall GdipCreateBitmapFromScan0(long long long long ptr ptr)
@ stdcall GdipCreateBitmapFromStream(ptr ptr)
@ stdcall GdipCreateBitmapFromStreamICM(ptr ptr)
@ stub GdipCreateCachedBitmap
@ stdcall GdipCreateCustomLineCap(ptr ptr long long ptr)
@ stub GdipCreateEffect
@ stub GdipCreateFont
@ stub GdipCreateFontFamilyFromName
@ stub GdipCreateFontFromDC
@ stdcall GdipCreateFontFromLogfontA(ptr ptr ptr)
@ stdcall GdipCreateFontFromLogfontW(ptr ptr ptr)
@ stdcall GdipCreateFromHDC2(long long ptr)
@ stdcall GdipCreateFromHDC(long ptr)
@ stdcall GdipCreateFromHWND(long ptr)
@ stub GdipCreateFromHWNDICM
@ stdcall GdipCreateHBITMAPFromBitmap(ptr ptr long)
@ stub GdipCreateHICONFromBitmap
@ stub GdipCreateHalftonePalette
@ stub GdipCreateHatchBrush
@ stdcall GdipCreateImageAttributes(ptr)
@ stdcall GdipCreateLineBrush(ptr ptr long long long ptr)
@ stub GdipCreateLineBrushFromRect
@ stdcall GdipCreateLineBrushFromRectI(ptr long long long long ptr)
@ stub GdipCreateLineBrushFromRectWithAngle
@ stub GdipCreateLineBrushFromRectWithAngleI
@ stub GdipCreateLineBrushI
@ stdcall GdipCreateMatrix2(long long long long long long ptr)
@ stdcall GdipCreateMatrix3(ptr ptr ptr)
@ stub GdipCreateMatrix3I
@ stdcall GdipCreateMatrix(ptr)
@ stdcall GdipCreateMetafileFromEmf(ptr long ptr)
@ stub GdipCreateMetafileFromFile
@ stub GdipCreateMetafileFromStream
@ stdcall GdipCreateMetafileFromWmf(ptr long ptr ptr)
@ stub GdipCreateMetafileFromWmfFile
@ stdcall GdipCreatePath2(ptr ptr long long ptr)
@ stub GdipCreatePath2I
@ stdcall GdipCreatePath(long ptr)
@ stdcall GdipCreatePathGradient(ptr long long ptr)
@ stdcall GdipCreatePathGradientFromPath(ptr ptr)
@ stub GdipCreatePathGradientI
@ stdcall GdipCreatePathIter(ptr ptr)
@ stdcall GdipCreatePen1(long long long ptr)
@ stdcall GdipCreatePen2(ptr long long ptr)
@ stub GdipCreateRegion
@ stub GdipCreateRegionHrgn
@ stub GdipCreateRegionPath
@ stub GdipCreateRegionRect
@ stub GdipCreateRegionRectI
@ stub GdipCreateRegionRgnData
@ stdcall GdipCreateSolidFill(long ptr)
@ stdcall GdipCreateStreamOnFile(ptr long ptr)
@ stdcall GdipCreateStringFormat(long long ptr)
@ stub GdipCreateTexture2
@ stub GdipCreateTexture2I
@ stub GdipCreateTexture
@ stdcall GdipCreateTextureIA(ptr ptr long long long long ptr)
@ stub GdipCreateTextureIAI
@ stdcall GdipDeleteBrush(ptr)
@ stub GdipDeleteCachedBitmap
@ stdcall GdipDeleteCustomLineCap(ptr)
@ stub GdipDeleteEffect
@ stdcall GdipDeleteFont(ptr)
@ stub GdipDeleteFontFamily
@ stdcall GdipDeleteGraphics(ptr)
@ stdcall GdipDeleteMatrix(ptr)
@ stdcall GdipDeletePath(ptr)
@ stdcall GdipDeletePathIter(ptr)
@ stdcall GdipDeletePen(ptr)
@ stub GdipDeletePrivateFontCollection
@ stub GdipDeleteRegion
@ stdcall GdipDeleteStringFormat(ptr)
@ stdcall GdipDisposeImage(ptr)
@ stdcall GdipDisposeImageAttributes(ptr)
@ stdcall GdipDrawArc(ptr ptr long long long long long long)
@ stdcall GdipDrawArcI(ptr ptr long long long long long long)
@ stdcall GdipDrawBezier(ptr ptr long long long long long long long long)
@ stdcall GdipDrawBezierI(ptr ptr long long long long long long long long)
@ stub GdipDrawBeziers
@ stub GdipDrawBeziersI
@ stub GdipDrawCachedBitmap
@ stub GdipDrawClosedCurve2
@ stub GdipDrawClosedCurve2I
@ stub GdipDrawClosedCurve
@ stub GdipDrawClosedCurveI
@ stdcall GdipDrawCurve2(ptr ptr ptr long long)
@ stub GdipDrawCurve2I
@ stub GdipDrawCurve3
@ stub GdipDrawCurve3I
@ stub GdipDrawCurve
@ stub GdipDrawCurveI
@ stub GdipDrawDriverString
@ stub GdipDrawEllipse
@ stub GdipDrawEllipseI
@ stub GdipDrawImage
@ stub GdipDrawImageFX
@ stdcall GdipDrawImageI(ptr ptr long long)
@ stub GdipDrawImagePointRect
@ stub GdipDrawImagePointRectI
@ stub GdipDrawImagePoints
@ stub GdipDrawImagePointsI
@ stdcall GdipDrawImagePointsRect(ptr ptr ptr long long long long long long ptr ptr ptr)
@ stub GdipDrawImagePointsRectI
@ stub GdipDrawImageRect
@ stub GdipDrawImageRectI
@ stdcall GdipDrawImageRectRect(ptr ptr long long long long long long long long long ptr long ptr)
@ stdcall GdipDrawImageRectRectI(ptr ptr long long long long long long long long long ptr long ptr)
@ stdcall GdipDrawLine(ptr ptr long long long long)
@ stdcall GdipDrawLineI(ptr ptr long long long long)
@ stdcall GdipDrawLines(ptr ptr ptr long)
@ stdcall GdipDrawLinesI(ptr ptr ptr long)
@ stdcall GdipDrawPath(ptr ptr ptr)
@ stdcall GdipDrawPie(ptr ptr long long long long long long)
@ stub GdipDrawPieI
@ stub GdipDrawPolygon
@ stub GdipDrawPolygonI
@ stub GdipDrawRectangle
@ stdcall GdipDrawRectangleI(ptr ptr long long long long)
@ stdcall GdipDrawRectangles(ptr ptr ptr long)
@ stub GdipDrawRectanglesI
@ stdcall GdipDrawString(ptr ptr long ptr ptr ptr ptr)
@ stub GdipEmfToWmfBits
@ stub GdipEndContainer
@ stub GdipEnumerateMetafileDestPoint
@ stub GdipEnumerateMetafileDestPointI
@ stub GdipEnumerateMetafileDestPoints
@ stub GdipEnumerateMetafileDestPointsI
@ stub GdipEnumerateMetafileDestRect
@ stub GdipEnumerateMetafileDestRectI
@ stub GdipEnumerateMetafileSrcRectDestPoint
@ stub GdipEnumerateMetafileSrcRectDestPointI
@ stub GdipEnumerateMetafileSrcRectDestPoints
@ stub GdipEnumerateMetafileSrcRectDestPointsI
@ stub GdipEnumerateMetafileSrcRectDestRect
@ stub GdipEnumerateMetafileSrcRectDestRectI
@ stub GdipFillClosedCurve2
@ stub GdipFillClosedCurve2I
@ stub GdipFillClosedCurve
@ stub GdipFillClosedCurveI
@ stub GdipFillEllipse
@ stub GdipFillEllipseI
@ stdcall GdipFillPath(ptr ptr ptr)
@ stdcall GdipFillPie(ptr ptr long long long long long long)
@ stub GdipFillPieI
@ stub GdipFillPolygon2
@ stub GdipFillPolygon2I
@ stdcall GdipFillPolygon(ptr ptr ptr long long)
@ stdcall GdipFillPolygonI(ptr ptr ptr long long)
@ stdcall GdipFillRectangle(ptr ptr long long long long)
@ stdcall GdipFillRectangleI(ptr ptr long long long long)
@ stub GdipFillRectangles
@ stub GdipFillRectanglesI
@ stub GdipFillRegion
@ stdcall GdipFindFirstImageItem(ptr ptr)
@ stub GdipFindNextImageItem
@ stub GdipFlattenPath
@ stub GdipFlush
@ stdcall GdipFree(ptr)
@ stub GdipGetAdjustableArrowCapFillState
@ stub GdipGetAdjustableArrowCapHeight
@ stub GdipGetAdjustableArrowCapMiddleInset
@ stub GdipGetAdjustableArrowCapWidth
@ stub GdipGetAllPropertyItems
@ stdcall GdipGetBrushType(ptr ptr)
@ stub GdipGetCellAscent
@ stub GdipGetCellDescent
@ stub GdipGetClip
@ stub GdipGetClipBounds
@ stub GdipGetClipBoundsI
@ stdcall GdipGetCompositingMode(ptr ptr)
@ stdcall GdipGetCompositingQuality(ptr ptr)
@ stub GdipGetCustomLineCapBaseCap
@ stdcall GdipGetCustomLineCapBaseInset(ptr ptr)
@ stub GdipGetCustomLineCapStrokeCaps
@ stub GdipGetCustomLineCapStrokeJoin
@ stub GdipGetCustomLineCapType
@ stub GdipGetCustomLineCapWidthScale
@ stub GdipGetDC
@ stub GdipGetDpiX
@ stub GdipGetDpiY
@ stub GdipGetEffectParameterSize
@ stub GdipGetEffectParameters
@ stub GdipGetEmHeight
@ stub GdipGetEncoderParameterList
@ stub GdipGetEncoderParameterListSize
@ stub GdipGetFamily
@ stub GdipGetFamilyName
@ stub GdipGetFontCollectionFamilyCount
@ stub GdipGetFontCollectionFamilyList
@ stub GdipGetFontHeight
@ stub GdipGetFontHeightGivenDPI
@ stub GdipGetFontSize
@ stub GdipGetFontStyle
@ stub GdipGetFontUnit
@ stub GdipGetGenericFontFamilyMonospace
@ stub GdipGetGenericFontFamilySansSerif
@ stub GdipGetGenericFontFamilySerif
@ stub GdipGetHatchBackgroundColor
@ stub GdipGetHatchForegroundColor
@ stub GdipGetHatchStyle
@ stub GdipGetHemfFromMetafile
@ stub GdipGetImageAttributesAdjustedPalette
@ stdcall GdipGetImageBounds(ptr ptr ptr)
@ stub GdipGetImageDecoders
@ stub GdipGetImageDecodersSize
@ stdcall GdipGetImageDimension(ptr ptr ptr)
@ stdcall GdipGetImageEncoders(long long ptr)
@ stdcall GdipGetImageEncodersSize(ptr ptr)
@ stub GdipGetImageFlags
@ stdcall GdipGetImageGraphicsContext(ptr ptr)
@ stdcall GdipGetImageHeight(ptr ptr)
@ stdcall GdipGetImageHorizontalResolution(ptr ptr)
@ stub GdipGetImageItemData
@ stub GdipGetImagePalette
@ stub GdipGetImagePaletteSize
@ stdcall GdipGetImagePixelFormat(ptr ptr)
@ stdcall GdipGetImageRawFormat(ptr ptr)
@ stub GdipGetImageThumbnail
@ stdcall GdipGetImageType(ptr ptr)
@ stdcall GdipGetImageVerticalResolution(ptr ptr)
@ stdcall GdipGetImageWidth(ptr ptr)
@ stdcall GdipGetInterpolationMode(ptr ptr)
@ stub GdipGetLineBlend
@ stub GdipGetLineBlendCount
@ stub GdipGetLineColors
@ stdcall GdipGetLineGammaCorrection(ptr ptr)
@ stub GdipGetLinePresetBlend
@ stub GdipGetLinePresetBlendCount
@ stub GdipGetLineRect
@ stub GdipGetLineRectI
@ stub GdipGetLineSpacing
@ stub GdipGetLineTransform
@ stub GdipGetLineWrapMode
@ stub GdipGetLogFontA
@ stdcall GdipGetLogFontW(ptr ptr ptr)
@ stdcall GdipGetMatrixElements(ptr ptr)
@ stub GdipGetMetafileDownLevelRasterizationLimit
@ stub GdipGetMetafileHeaderFromEmf
@ stub GdipGetMetafileHeaderFromFile
@ stdcall GdipGetMetafileHeaderFromMetafile(ptr ptr)
@ stub GdipGetMetafileHeaderFromStream
@ stub GdipGetMetafileHeaderFromWmf
@ stub GdipGetNearestColor
@ stdcall GdipGetPageScale(ptr ptr)
@ stdcall GdipGetPageUnit(ptr ptr)
@ stub GdipGetPathData
@ stdcall GdipGetPathFillMode(ptr ptr)
@ stub GdipGetPathGradientBlend
@ stub GdipGetPathGradientBlendCount
@ stub GdipGetPathGradientCenterColor
@ stdcall GdipGetPathGradientCenterPoint(ptr ptr)
@ stub GdipGetPathGradientCenterPointI
@ stdcall GdipGetPathGradientFocusScales(ptr ptr ptr)
@ stdcall GdipGetPathGradientGammaCorrection(ptr ptr)
@ stub GdipGetPathGradientPath
@ stdcall GdipGetPathGradientPointCount(ptr ptr)
@ stub GdipGetPathGradientPresetBlend
@ stub GdipGetPathGradientPresetBlendCount
@ stub GdipGetPathGradientRect
@ stub GdipGetPathGradientRectI
@ stub GdipGetPathGradientSurroundColorCount
@ stdcall GdipGetPathGradientSurroundColorsWithCount(ptr ptr ptr)
@ stub GdipGetPathGradientTransform
@ stub GdipGetPathGradientWrapMode
@ stub GdipGetPathLastPoint
@ stdcall GdipGetPathPoints(ptr ptr long)
@ stub GdipGetPathPointsI
@ stdcall GdipGetPathTypes(ptr ptr long)
@ stdcall GdipGetPathWorldBounds(ptr ptr ptr ptr)
@ stub GdipGetPathWorldBoundsI
@ stdcall GdipGetPenBrushFill(ptr ptr)
@ stdcall GdipGetPenColor(ptr ptr)
@ stub GdipGetPenCompoundArray
@ stub GdipGetPenCompoundCount
@ stub GdipGetPenCustomEndCap
@ stub GdipGetPenCustomStartCap
@ stdcall GdipGetPenDashArray(ptr ptr long)
@ stub GdipGetPenDashCap197819
@ stub GdipGetPenDashCount
@ stdcall GdipGetPenDashOffset(ptr ptr)
@ stdcall GdipGetPenDashStyle(ptr ptr)
@ stub GdipGetPenEndCap
@ stub GdipGetPenFillType
@ stub GdipGetPenLineJoin
@ stub GdipGetPenMiterLimit
@ stub GdipGetPenMode
@ stub GdipGetPenStartCap
@ stub GdipGetPenTransform
@ stub GdipGetPenUnit
@ stub GdipGetPenWidth
@ stdcall GdipGetPixelOffsetMode(ptr ptr)
@ stdcall GdipGetPointCount(ptr ptr)
@ stub GdipGetPropertyCount
@ stub GdipGetPropertyIdList
@ stub GdipGetPropertyItem
@ stdcall GdipGetPropertyItemSize(ptr long ptr)
@ stub GdipGetPropertySize
@ stub GdipGetRegionBounds
@ stub GdipGetRegionBoundsI
@ stub GdipGetRegionData
@ stub GdipGetRegionDataSize
@ stub GdipGetRegionHRgn
@ stub GdipGetRegionScans
@ stub GdipGetRegionScansCount
@ stub GdipGetRegionScansI
@ stub GdipGetRenderingOrigin
@ stdcall GdipGetSmoothingMode(ptr ptr)
@ stdcall GdipGetSolidFillColor(ptr ptr)
@ stdcall GdipGetStringFormatAlign(ptr ptr)
@ stub GdipGetStringFormatDigitSubstitution
@ stub GdipGetStringFormatFlags
@ stdcall GdipGetStringFormatHotkeyPrefix(ptr ptr)
@ stdcall GdipGetStringFormatLineAlign(ptr ptr)
@ stub GdipGetStringFormatMeasurableCharacterRangeCount
@ stub GdipGetStringFormatTabStopCount
@ stub GdipGetStringFormatTabStops
@ stdcall GdipGetStringFormatTrimming(ptr ptr)
@ stub GdipGetTextContrast
@ stdcall GdipGetTextRenderingHint(ptr ptr)
@ stub GdipGetTextureImage
@ stub GdipGetTextureTransform
@ stub GdipGetTextureWrapMode
@ stub GdipGetVisibleClipBounds
@ stub GdipGetVisibleClipBoundsI
@ stdcall GdipGetWorldTransform(ptr ptr)
@ stub GdipGraphicsClear
@ stub GdipGraphicsSetAbort
@ stub GdipImageForceValidation
@ stdcall GdipImageGetFrameCount(ptr ptr ptr)
@ stub GdipImageGetFrameDimensionsCount
@ stdcall GdipImageGetFrameDimensionsList(ptr ptr long)
@ stub GdipImageRotateFlip
@ stdcall GdipImageSelectActiveFrame(ptr ptr long)
@ stub GdipImageSetAbort
@ stub GdipInitializePalette
@ stub GdipInvertMatrix
@ stub GdipIsClipEmpty
@ stub GdipIsEmptyRegion
@ stub GdipIsEqualRegion
@ stub GdipIsInfiniteRegion
@ stub GdipIsMatrixEqual
@ stub GdipIsMatrixIdentity
@ stub GdipIsMatrixInvertible
@ stub GdipIsOutlineVisiblePathPoint
@ stdcall GdipIsOutlineVisiblePathPointI(ptr long long ptr ptr ptr)
@ stub GdipIsStyleAvailable
@ stub GdipIsVisibleClipEmpty
@ stub GdipIsVisiblePathPoint
@ stub GdipIsVisiblePathPointI
@ stub GdipIsVisiblePoint
@ stub GdipIsVisiblePointI
@ stub GdipIsVisibleRect
@ stub GdipIsVisibleRectI
@ stub GdipIsVisibleRegionPoint
@ stub GdipIsVisibleRegionPointI
@ stub GdipIsVisibleRegionRect
@ stub GdipIsVisibleRegionRectI
@ stdcall GdipLoadImageFromFile(wstr ptr)
@ stub GdipLoadImageFromFileICM
@ stdcall GdipLoadImageFromStream(ptr ptr)
@ stdcall GdipLoadImageFromStreamICM(ptr ptr)
@ stub GdipMeasureCharacterRanges
@ stub GdipMeasureDriverString
@ stdcall GdipMeasureString(ptr ptr long ptr ptr ptr ptr ptr ptr)
@ stub GdipMultiplyLineTransform
@ stdcall GdipMultiplyMatrix(ptr ptr long)
@ stub GdipMultiplyPathGradientTransform
@ stub GdipMultiplyPenTransform
@ stub GdipMultiplyTextureTransform
@ stub GdipMultiplyWorldTransform
@ stub GdipNewInstalledFontCollection
@ stub GdipNewPrivateFontCollection
@ stdcall GdipPathIterCopyData(ptr ptr ptr ptr long long)
@ stub GdipPathIterEnumerate
@ stub GdipPathIterGetCount
@ stub GdipPathIterGetSubpathCount
@ stub GdipPathIterHasCurve
@ stub GdipPathIterIsValid
@ stub GdipPathIterNextMarker
@ stub GdipPathIterNextMarkerPath
@ stub GdipPathIterNextPathType
@ stdcall GdipPathIterNextSubpath(ptr ptr ptr ptr ptr)
@ stub GdipPathIterNextSubpathPath
@ stdcall GdipPathIterRewind(ptr)
@ stub GdipPlayMetafileRecord
@ stub GdipPlayTSClientRecord
@ stub GdipPrivateAddFontFile
@ stub GdipPrivateAddMemoryFont
@ stub GdipRecordMetafile
@ stub GdipRecordMetafileFileName
@ stub GdipRecordMetafileFileNameI
@ stub GdipRecordMetafileI
@ stub GdipRecordMetafileStream
@ stub GdipRecordMetafileStreamI
@ stub GdipReleaseDC
@ stdcall GdipRemovePropertyItem(ptr long)
@ stub GdipResetClip
@ stub GdipResetImageAttributes
@ stub GdipResetLineTransform
@ stub GdipResetPageTransform
@ stdcall GdipResetPath(ptr)
@ stub GdipResetPathGradientTransform
@ stub GdipResetPenTransform
@ stub GdipResetTextureTransform
@ stub GdipResetWorldTransform
@ stdcall GdipRestoreGraphics(ptr long)
@ stub GdipReversePath
@ stub GdipRotateLineTransform
@ stdcall GdipRotateMatrix(ptr long long)
@ stub GdipRotatePathGradientTransform
@ stub GdipRotatePenTransform
@ stub GdipRotateTextureTransform
@ stdcall GdipRotateWorldTransform(ptr long long)
@ stub GdipSaveAdd
@ stub GdipSaveAddImage
@ stdcall GdipSaveGraphics(ptr ptr)
@ stdcall GdipSaveImageToFile(ptr ptr ptr ptr)
@ stdcall GdipSaveImageToStream(ptr ptr ptr ptr)
@ stub GdipScaleLineTransform
@ stdcall GdipScaleMatrix(ptr long long long)
@ stub GdipScalePathGradientTransform
@ stub GdipScalePenTransform
@ stub GdipScaleTextureTransform
@ stdcall GdipScaleWorldTransform(ptr long long long)
@ stub GdipSetAdjustableArrowCapFillState
@ stub GdipSetAdjustableArrowCapHeight
@ stub GdipSetAdjustableArrowCapMiddleInset
@ stub GdipSetAdjustableArrowCapWidth
@ stub GdipSetClipGraphics
@ stub GdipSetClipHrgn
@ stub GdipSetClipPath
@ stub GdipSetClipRect
@ stdcall GdipSetClipRectI(ptr long long long long long)
@ stdcall GdipSetClipRegion(ptr ptr long)
@ stdcall GdipSetCompositingMode(ptr long)
@ stdcall GdipSetCompositingQuality(ptr long)
@ stdcall GdipSetCustomLineCapBaseCap(ptr long)
@ stdcall GdipSetCustomLineCapBaseInset(ptr long)
@ stdcall GdipSetCustomLineCapStrokeCaps(ptr long long)
@ stdcall GdipSetCustomLineCapStrokeJoin(ptr long)
@ stdcall GdipSetCustomLineCapWidthScale(ptr long)
@ stdcall GdipSetEffectParameters(ptr ptr long)
@ stdcall GdipSetEmpty(ptr)
@ stdcall GdipSetImageAttributesCachedBackground(ptr long)
@ stdcall GdipSetImageAttributesColorKeys(ptr long long long long)
@ stdcall GdipSetImageAttributesColorMatrix(ptr long long ptr ptr long)
@ stdcall GdipSetImageAttributesGamma(ptr long long long)
@ stdcall GdipSetImageAttributesNoOp(ptr long long)
@ stdcall GdipSetImageAttributesOutputChannel(ptr long long long)
@ stdcall GdipSetImageAttributesOutputChannelColorProfile(ptr long long ptr)
@ stdcall GdipSetImageAttributesRemapTable(ptr long long long ptr)
@ stdcall GdipSetImageAttributesThreshold(ptr long long long)
@ stdcall GdipSetImageAttributesToIdentity(ptr long)
@ stdcall GdipSetImageAttributesWrapMode(ptr long long long)
@ stdcall GdipSetImagePalette(ptr ptr)
@ stdcall GdipSetInfinite(ptr)
@ stdcall GdipSetInterpolationMode(ptr long)
@ stdcall GdipSetLineBlend(ptr ptr ptr long)
@ stub GdipSetLineColors
@ stdcall GdipSetLineGammaCorrection(ptr long)
@ stub GdipSetLineLinearBlend
@ stub GdipSetLinePresetBlend
@ stdcall GdipSetLineSigmaBlend(ptr long long)
@ stub GdipSetLineTransform
@ stdcall GdipSetLineWrapMode(ptr long)
@ stdcall GdipSetMatrixElements(ptr long long long long long long)
@ stub GdipSetMetafileDownLevelRasterizationLimit
@ stdcall GdipSetPageScale(ptr long)
@ stdcall GdipSetPageUnit(ptr long)
@ stdcall GdipSetPathFillMode(ptr long)
@ stub GdipSetPathGradientBlend
@ stdcall GdipSetPathGradientCenterColor(ptr long)
@ stdcall GdipSetPathGradientCenterPoint(ptr ptr)
@ stub GdipSetPathGradientCenterPointI
@ stdcall GdipSetPathGradientFocusScales(ptr long long)
@ stdcall GdipSetPathGradientGammaCorrection(ptr long)
@ stub GdipSetPathGradientLinearBlend
@ stub GdipSetPathGradientPath
@ stub GdipSetPathGradientPresetBlend
@ stdcall GdipSetPathGradientSigmaBlend(ptr long long)
@ stdcall GdipSetPathGradientSurroundColorsWithCount(ptr ptr ptr)
@ stub GdipSetPathGradientTransform
@ stdcall GdipSetPathGradientWrapMode(ptr long)
@ stub GdipSetPathMarker
@ stdcall GdipSetPenBrushFill(ptr ptr)
@ stdcall GdipSetPenColor(ptr long)
@ stub GdipSetPenCompoundArray
@ stdcall GdipSetPenCustomEndCap(ptr ptr)
@ stdcall GdipSetPenCustomStartCap(ptr ptr)
@ stdcall GdipSetPenDashArray(ptr ptr long)
@ stub GdipSetPenDashCap197819
@ stdcall GdipSetPenDashOffset(ptr long)
@ stdcall GdipSetPenDashStyle(ptr long)
@ stdcall GdipSetPenEndCap(ptr long)
@ stdcall GdipSetPenLineCap197819(ptr long long long)
@ stdcall GdipSetPenLineJoin(ptr long)
@ stdcall GdipSetPenMiterLimit(ptr long)
@ stdcall GdipSetPenMode(ptr long)
@ stdcall GdipSetPenStartCap(ptr long)
@ stub GdipSetPenTransform
@ stub GdipSetPenUnit
@ stdcall GdipSetPenWidth(ptr long)
@ stdcall GdipSetPixelOffsetMode(ptr long)
@ stub GdipSetPropertyItem
@ stub GdipSetRenderingOrigin
@ stdcall GdipSetSmoothingMode(ptr long)
@ stdcall GdipSetSolidFillColor(ptr ptr)
@ stdcall GdipSetStringFormatAlign(ptr long)
@ stub GdipSetStringFormatDigitSubstitution
@ stdcall GdipSetStringFormatFlags(ptr long)
@ stdcall GdipSetStringFormatHotkeyPrefix(ptr long)
@ stdcall GdipSetStringFormatLineAlign(ptr long)
@ stub GdipSetStringFormatMeasurableCharacterRanges
@ stub GdipSetStringFormatTabStops
@ stdcall GdipSetStringFormatTrimming(ptr long)
@ stub GdipSetTextContrast
@ stdcall GdipSetTextRenderingHint(ptr long)
@ stdcall GdipSetTextureTransform(ptr ptr)
@ stub GdipSetTextureWrapMode
@ stdcall GdipSetWorldTransform(ptr ptr)
@ stub GdipShearMatrix
@ stdcall GdipStartPathFigure(ptr)
@ stub GdipStringFormatGetGenericDefault
@ stub GdipStringFormatGetGenericTypographic
@ stub GdipTestControl
@ stdcall GdipTransformMatrixPoints(ptr ptr long)
@ stub GdipTransformMatrixPointsI
@ stdcall GdipTransformPath(ptr ptr)
@ stub GdipTransformPoints
@ stub GdipTransformPointsI
@ stub GdipTransformRegion
@ stub GdipTranslateClip
@ stub GdipTranslateClipI
@ stub GdipTranslateLineTransform
@ stdcall GdipTranslateMatrix(ptr long long long)
@ stub GdipTranslatePathGradientTransform
@ stub GdipTranslatePenTransform
@ stub GdipTranslateRegion
@ stub GdipTranslateRegionI
@ stub GdipTranslateTextureTransform
@ stdcall GdipTranslateWorldTransform(ptr long long long)
@ stub GdipVectorTransformMatrixPoints
@ stub GdipVectorTransformMatrixPointsI
@ stub GdipWarpPath
@ stub GdipWidenPath
@ stub GdipWindingModeOutline
@ stub GdiplusNotificationHook
@ stub GdiplusNotificationUnhook
@ stdcall GdiplusShutdown(ptr)
@ stdcall GdiplusStartup(ptr ptr ptr)
