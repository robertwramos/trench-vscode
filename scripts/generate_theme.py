#!/usr/bin/env python3
"""Generate the Trench VS Code theme (palette adapted from the Mariana color scheme)."""
import colorsys
import json
import os
import sys

OUT = sys.argv[1]


def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return "#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))


def A(hexcolor, alpha):
    """Return #RRGGBBAA for a #RRGGBB color and 0-1 alpha."""
    return hexcolor[:7] + "%02X" % round(alpha * 255)


# --- Palette: variables from Mariana.sublime-color-scheme -------------------
black = "#000000"
blue = hsl(210, 50, 60)
blue_vibrant = hsl(210, 60, 60)
blue2 = hsl(210, 13, 40)  # used at alpha 0.7 in the scheme
blue3 = hsl(210, 15, 22)  # background
blue4 = hsl(210, 13, 45)  # selection_border
blue5 = hsl(180, 36, 54)  # teal
blue6 = hsl(221, 12, 69)  # comments
green = hsl(114, 31, 68)
grey = hsl(0, 0, 20)
orange = hsl(32, 93, 66)
orange2 = hsl(32, 85, 55)
orange3 = hsl(40, 94, 68)
pink = hsl(300, 30, 68)
red = hsl(357, 79, 65)
red2 = hsl(13, 93, 66)
white = "#FFFFFF"
white2 = hsl(0, 0, 97)
white3 = hsl(219, 28, 88)

# --- Derived shades (Mariana's UI theme uses darker chrome around the editor)
bg = blue3
bg_side = hsl(210, 15, 19)
bg_deep = hsl(210, 15, 16)
bg_deeper = hsl(210, 15, 13)
bg_raise = hsl(210, 15, 26)
bg_raise2 = hsl(210, 15, 30)
dim = hsl(215, 12, 58)  # between blue4 and blue6, for inactive text
border = hsl(210, 15, 13)
sel = A(blue2, 0.7)  # selection / line_highlight
green_br = hsl(114, 40, 76)
red_br = hsl(357, 90, 74)
blue_br = hsl(210, 70, 70)
pink_br = hsl(300, 40, 76)
cyan_br = hsl(180, 45, 66)
yellow = orange3

transparent = "#00000000"

c = {}


def put(keys, value):
    for k in keys.split():
        c[k] = value


# ---------------------------------------------------------------- base
put("foreground", white3)
put("disabledForeground", blue4)
put("errorForeground", red)
put("descriptionForeground", blue6)
put("icon.foreground", blue6)
put("focusBorder", blue_vibrant)
put("contrastBorder", transparent)
put("contrastActiveBorder", transparent)
put("selection.background", A(blue_vibrant, 0.5))
put("textBlockQuote.background", bg_deep)
put("textBlockQuote.border", blue5)
put("textCodeBlock.background", A(blue2, 0.5))
put("textLink.foreground", blue)
put("textLink.activeForeground", blue_br)
put("textPreformat.foreground", orange)
put("textPreformat.background", A(blue2, 0.5))
put("textPreformat.border", transparent)
put("textSeparator.foreground", blue4)
put("toolbar.hoverBackground", A(blue2, 0.5))
put("toolbar.hoverOutline", transparent)
put("toolbar.activeBackground", A(blue2, 0.7))
put("widget.shadow", A(black, 0.25))
put("widget.border", border)
put("sash.hoverBorder", blue_vibrant)
put("scrollbar.shadow", A(black, 0.25))
put("scrollbarSlider.background", A(blue4, 0.35))
put("scrollbarSlider.hoverBackground", A(blue4, 0.55))
put("scrollbarSlider.activeBackground", A(blue4, 0.75))
put("progressBar.background", blue_vibrant)
put("window.activeBorder", transparent)
put("window.inactiveBorder", transparent)

# ---------------------------------------------------------------- buttons / inputs
put("button.background", blue_vibrant)
put("button.foreground", bg_deeper)
put("button.hoverBackground", blue_br)
put("button.border", transparent)
put("button.separator", A(bg_deeper, 0.4))
put("button.secondaryBackground", bg_raise2)
put("button.secondaryForeground", white3)
put("button.secondaryHoverBackground", hsl(210, 15, 36))
put("checkbox.background", bg_deep)
put("checkbox.foreground", white3)
put("checkbox.border", blue4)
put("checkbox.selectBackground", bg_raise)
put("checkbox.selectBorder", blue5)
put("dropdown.background", bg_deep)
put("dropdown.listBackground", bg_raise)
put("dropdown.border", border)
put("dropdown.foreground", white3)
put("input.background", bg_deep)
put("input.border", border)
put("input.foreground", white3)
put("input.placeholderForeground", blue4)
put("inputOption.activeBackground", A(blue_vibrant, 0.35))
put("inputOption.activeBorder", blue_vibrant)
put("inputOption.activeForeground", white)
put("inputOption.hoverBackground", A(blue2, 0.5))
put("inputValidation.errorBackground", hsl(357, 40, 22))
put("inputValidation.errorForeground", white3)
put("inputValidation.errorBorder", red)
put("inputValidation.infoBackground", hsl(210, 40, 24))
put("inputValidation.infoForeground", white3)
put("inputValidation.infoBorder", blue)
put("inputValidation.warningBackground", hsl(32, 40, 22))
put("inputValidation.warningForeground", white3)
put("inputValidation.warningBorder", orange)
put("radio.activeBackground", A(blue_vibrant, 0.35))
put("radio.activeForeground", white)
put("radio.activeBorder", blue_vibrant)
put("radio.inactiveBackground", transparent)
put("radio.inactiveForeground", blue6)
put("radio.inactiveBorder", blue4)
put("radio.inactiveHoverBackground", A(blue2, 0.5))
put("keybindingLabel.background", bg_deep)
put("keybindingLabel.foreground", white3)
put("keybindingLabel.border", border)
put("keybindingLabel.bottomBorder", bg_deeper)
put("keybindingTable.headerBackground", bg_raise)
put("keybindingTable.rowsBackground", bg_side)

# ---------------------------------------------------------------- badges
put("badge.background", blue_vibrant)
put("badge.foreground", bg_deeper)
put("activityBarBadge.background", orange)
put("activityBarBadge.foreground", bg_deeper)
put("activityBarTop.background", bg_deep)
put("activityBarTop.foreground", white3)
put("activityBarTop.inactiveForeground", dim)
put("activityBarTop.activeBorder", blue5)
put("activityBarTop.activeBackground", transparent)
put("activityBarTop.dropBorder", white3)
put("activityWarningBadge.background", orange2)
put("activityWarningBadge.foreground", bg_deeper)
put("activityErrorBadge.background", red)
put("activityErrorBadge.foreground", bg_deeper)
put("profileBadge.background", orange)
put("profileBadge.foreground", bg_deeper)
put("extensionBadge.remoteBackground", blue_vibrant)
put("extensionBadge.remoteForeground", bg_deeper)

# ---------------------------------------------------------------- lists / trees
put("list.activeSelectionBackground", sel)
put("list.activeSelectionForeground", white)
put("list.activeSelectionIconForeground", white)
put("list.inactiveSelectionBackground", A(blue2, 0.5))
put("list.inactiveSelectionForeground", white3)
put("list.inactiveSelectionIconForeground", white3)
put("list.focusBackground", sel)
put("list.focusForeground", white)
put("list.focusOutline", blue_vibrant)
put("list.focusAndSelectionOutline", blue_vibrant)
put("list.inactiveFocusBackground", A(blue2, 0.5))
put("list.inactiveFocusOutline", transparent)
put("list.hoverBackground", A(blue2, 0.35))
put("list.hoverForeground", white3)
put("list.highlightForeground", orange3)
put("list.focusHighlightForeground", orange3)
put("list.dropBackground", A(blue_vibrant, 0.25))
put("list.dropBetweenBackground", blue_vibrant)
put("list.errorForeground", red)
put("list.warningForeground", orange)
put("list.invalidItemForeground", red)
put("list.deemphasizedForeground", blue4)
put("list.filterMatchBackground", A(orange3, 0.3))
put("list.filterMatchBorder", orange3)
put("listFilterWidget.background", bg_raise)
put("listFilterWidget.outline", blue_vibrant)
put("listFilterWidget.noMatchesOutline", red)
put("listFilterWidget.shadow", A(black, 0.25))
put("tree.indentGuidesStroke", A(blue5, 0.35))
put("tree.inactiveIndentGuidesStroke", A(blue5, 0.15))
put("tree.tableColumnsBorder", A(blue4, 0.3))
put("tree.tableOddRowsBackground", A(white, 0.03))

# ---------------------------------------------------------------- activity bar / side bar
put("activityBar.background", bg_deep)
put("activityBar.foreground", white3)
put("activityBar.inactiveForeground", dim)
put("activityBar.border", border)
put("activityBar.activeBorder", blue5)
put("activityBar.activeBackground", transparent)
put("activityBar.activeFocusBorder", blue_vibrant)
put("activityBar.dropBorder", white3)
put("sideBar.background", bg_side)
put("sideBar.foreground", blue6)
put("sideBar.border", border)
put("sideBar.dropBackground", A(blue_vibrant, 0.25))
put("sideBarTitle.foreground", white3)
put("sideBarTitle.background", bg_side)
put("sideBarTitle.border", border)
put("sideBarSectionHeader.background", bg_deep)
put("sideBarSectionHeader.foreground", white3)
put("sideBarSectionHeader.border", border)
put("sideBarActivityBarTop.border", border)
put("sideBarStickyScroll.background", bg_side)
put("sideBarStickyScroll.border", border)
put("sideBarStickyScroll.shadow", A(black, 0.25))
put("secondarySideBar.background", bg_side)
put("secondarySideBar.foreground", blue6)
put("secondarySideBar.border", border)
put("secondarySideBar.dropBackground", A(blue_vibrant, 0.25))
put("secondarySideBarSectionHeader.background", bg_deep)
put("secondarySideBarSectionHeader.foreground", white3)
put("secondarySideBarSectionHeader.border", border)
put("secondarySideBarTitle.foreground", white3)
put("secondarySideBarTitle.background", bg_side)
put("secondarySideBarTitle.border", border)

# ---------------------------------------------------------------- minimap
put("minimap.background", bg)
put("minimap.findMatchHighlight", A(orange3, 0.8))
put("minimap.selectionHighlight", A(blue_vibrant, 0.6))
put("minimap.selectionOccurrenceHighlight", A(blue5, 0.5))
put("minimap.errorHighlight", red)
put("minimap.warningHighlight", orange)
put("minimap.infoHighlight", blue)
put("minimap.foregroundOpacity", "#000000B3")
put("minimap.chatEditHighlight", A(blue2, 0.6))
put("minimapSlider.background", A(blue4, 0.2))
put("minimapSlider.hoverBackground", A(blue4, 0.35))
put("minimapSlider.activeBackground", A(blue4, 0.5))
put("minimapGutter.addedBackground", green)
put("minimapGutter.modifiedBackground", orange)
put("minimapGutter.deletedBackground", red)

# ---------------------------------------------------------------- editor groups / tabs
put("editorGroup.border", border)
put("editorGroup.dropBackground", A(blue_vibrant, 0.2))
put("editorGroup.dropIntoPromptForeground", white3)
put("editorGroup.dropIntoPromptBackground", bg_raise)
put("editorGroup.dropIntoPromptBorder", transparent)
put("editorGroup.emptyBackground", bg)
put("editorGroup.focusedEmptyBorder", blue_vibrant)
put("editorGroupHeader.noTabsBackground", bg)
put("editorGroupHeader.tabsBackground", bg_deep)
put("editorGroupHeader.tabsBorder", border)
put("editorGroupHeader.border", border)
put("tab.activeBackground", bg)
put("tab.activeForeground", white)
put("tab.activeBorder", transparent)
put("tab.activeBorderTop", blue5)
put("tab.activeModifiedBorder", orange)
put("tab.border", border)
put("tab.hoverBackground", bg_raise)
put("tab.hoverForeground", white)
put("tab.hoverBorder", transparent)
put("tab.inactiveBackground", bg_deep)
put("tab.inactiveForeground", dim)
put("tab.inactiveModifiedBorder", A(orange, 0.5))
put("tab.lastPinnedBorder", blue4)
put("tab.selectedBackground", bg)
put("tab.selectedForeground", white)
put("tab.selectedBorderTop", blue5)
put("tab.unfocusedActiveBackground", bg)
put("tab.unfocusedActiveForeground", blue6)
put("tab.unfocusedActiveBorder", transparent)
put("tab.unfocusedActiveBorderTop", A(blue5, 0.5))
put("tab.unfocusedActiveModifiedBorder", A(orange, 0.5))
put("tab.unfocusedHoverBackground", bg_raise)
put("tab.unfocusedHoverForeground", white3)
put("tab.unfocusedHoverBorder", transparent)
put("tab.unfocusedInactiveBackground", bg_deep)
put("tab.unfocusedInactiveForeground", blue4)
put("tab.unfocusedInactiveModifiedBorder", A(orange, 0.3))

# ---------------------------------------------------------------- editor core
put("editor.background", bg)
put("editor.foreground", white3)
put("editorLineNumber.foreground", blue4)
put("editorLineNumber.activeForeground", blue6)
put("editorLineNumber.dimmedForeground", A(blue4, 0.5))
put("editorCursor.foreground", orange)
put("editorCursor.background", bg)
put("editorMultiCursor.primary.foreground", orange)
put("editorMultiCursor.primary.background", bg)
put("editorMultiCursor.secondary.foreground", orange2)
put("editorMultiCursor.secondary.background", bg)
put("editor.selectionBackground", sel)
put("editor.inactiveSelectionBackground", A(blue2, 0.5))
put("editor.selectionHighlightBackground", A(blue5, 0.2))
put("editor.selectionHighlightBorder", A(blue5, 0.4))
put("editor.wordHighlightBackground", A(blue5, 0.2))
put("editor.wordHighlightBorder", transparent)
put("editor.wordHighlightStrongBackground", A(blue5, 0.35))
put("editor.wordHighlightStrongBorder", transparent)
put("editor.wordHighlightTextBackground", A(blue5, 0.2))
put("editor.wordHighlightTextBorder", transparent)
put("editor.findMatchBackground", orange3)
put("editor.findMatchForeground", grey)
put("editor.findMatchBorder", orange3)
put("editor.findMatchHighlightBackground", A(orange3, 0.35))
put("editor.findMatchHighlightForeground", white)
put("editor.findMatchHighlightBorder", transparent)
put("editor.findRangeHighlightBackground", A(blue2, 0.4))
put("editor.findRangeHighlightBorder", transparent)
put("editor.hoverHighlightBackground", A(blue2, 0.5))
put("editor.lineHighlightBackground", A(blue2, 0.3))
put("editor.lineHighlightBorder", transparent)
put("editor.rangeHighlightBackground", A(blue2, 0.3))
put("editor.rangeHighlightBorder", transparent)
put("editor.symbolHighlightBackground", A(blue5, 0.25))
put("editor.symbolHighlightBorder", transparent)
put("editor.linkedEditingBackground", A(blue5, 0.2))
put("editor.placeholder.foreground", blue4)
put("editor.compositionBorder", blue_vibrant)
put("editor.foldBackground", A(blue2, 0.25))
put("editor.foldPlaceholderForeground", blue6)
put("editor.foldControlForeground", blue6)
put("editor.inlineValuesForeground", blue4)
put("editor.inlineValuesBackground", A(blue2, 0.3))
put("editor.snippetTabstopHighlightBackground", A(blue5, 0.2))
put("editor.snippetTabstopHighlightBorder", transparent)
put("editor.snippetFinalTabstopHighlightBackground", transparent)
put("editor.snippetFinalTabstopHighlightBorder", blue5)
put("editor.stackFrameHighlightBackground", A(orange3, 0.2))
put("editor.focusedStackFrameHighlightBackground", A(green, 0.25))
put("editorLink.activeForeground", blue)
put("editorWhitespace.foreground", A(blue4, 0.5))
put("editorRuler.foreground", A(blue4, 0.4))
put("editorCodeLens.foreground", blue4)
put("editorLightBulb.foreground", orange3)
put("editorLightBulbAutoFix.foreground", blue5)
put("editorLightBulbAi.foreground", pink)
put("editorUnicodeHighlight.border", orange)
put("editorUnicodeHighlight.background", A(orange, 0.15))
put("editorUnnecessaryCode.border", transparent)
put("editorUnnecessaryCode.opacity", "#00000080")
put("editorHint.foreground", blue5)
put("editorHint.border", transparent)
put("editorInlayHint.foreground", blue4)
put("editorInlayHint.background", A(blue2, 0.25))
put("editorInlayHint.typeForeground", blue4)
put("editorInlayHint.typeBackground", A(blue2, 0.25))
put("editorInlayHint.parameterForeground", blue4)
put("editorInlayHint.parameterBackground", A(blue2, 0.25))
put("editorGhostText.foreground", A(blue6, 0.5))
put("editorGhostText.background", transparent)
put("editorGhostText.border", transparent)
put("editorError.foreground", red)
put("editorError.border", transparent)
put("editorError.background", transparent)
put("editorWarning.foreground", orange)
put("editorWarning.border", transparent)
put("editorWarning.background", transparent)
put("editorInfo.foreground", blue)
put("editorInfo.border", transparent)
put("editorInfo.background", transparent)
put("problemsErrorIcon.foreground", red)
put("problemsWarningIcon.foreground", orange)
put("problemsInfoIcon.foreground", blue)

# indent guides, bracket matching (stack_guide / active_guide / brackets_*)
for i in range(1, 7):
    put("editorIndentGuide.background%d" % i, A(blue5, 0.2))
    put("editorIndentGuide.activeBackground%d" % i, A(blue5, 0.7))
    put("editorBracketPairGuide.background%d" % i, A(blue5, 0.2))
    put("editorBracketPairGuide.activeBackground%d" % i, A(blue5, 0.7))
for i, col in enumerate([orange, blue5, pink, green, blue, red2], 1):
    put("editorBracketHighlight.foreground%d" % i, col)
put("editorBracketHighlight.unexpectedBracket.foreground", red)
put("editorBracketMatch.background", A(orange, 0.15))
put("editorBracketMatch.border", orange)

# gutter
put("editorGutter.background", bg)
put("editorGutter.modifiedBackground", orange)
put("editorGutter.addedBackground", green)
put("editorGutter.deletedBackground", red)
put("editorGutter.commentRangeForeground", blue4)
put("editorGutter.commentGlyphsForeground", blue6)
put("editorGutter.commentUnresolvedGlyphsForeground", orange)
put("editorGutter.foldingControlForeground", blue6)
put("editorCommentsWidget.resolvedBorder", blue4)
put("editorCommentsWidget.unresolvedBorder", orange)
put("editorCommentsWidget.rangeBackground", A(blue2, 0.3))
put("editorCommentsWidget.rangeActiveBackground", A(blue2, 0.5))
put("editorCommentsWidget.replyInputBackground", bg_deep)

# sticky scroll
put("editorStickyScroll.background", bg)
put("editorStickyScroll.border", border)
put("editorStickyScroll.shadow", A(black, 0.25))
put("editorStickyScrollHover.background", bg_raise)
put("editorStickyScrollGutter.background", bg)

# overview ruler
put("editorOverviewRuler.border", transparent)
put("editorOverviewRuler.background", bg)
put("editorOverviewRuler.findMatchForeground", A(orange3, 0.8))
put("editorOverviewRuler.rangeHighlightForeground", A(blue2, 0.8))
put("editorOverviewRuler.selectionHighlightForeground", A(blue5, 0.6))
put("editorOverviewRuler.wordHighlightForeground", A(blue5, 0.5))
put("editorOverviewRuler.wordHighlightStrongForeground", A(blue5, 0.7))
put("editorOverviewRuler.wordHighlightTextForeground", A(blue5, 0.5))
put("editorOverviewRuler.modifiedForeground", A(orange, 0.8))
put("editorOverviewRuler.addedForeground", A(green, 0.8))
put("editorOverviewRuler.deletedForeground", A(red, 0.8))
put("editorOverviewRuler.errorForeground", red)
put("editorOverviewRuler.warningForeground", orange)
put("editorOverviewRuler.infoForeground", blue)
put("editorOverviewRuler.bracketMatchForeground", orange)
put("editorOverviewRuler.currentContentForeground", A(green, 0.6))
put("editorOverviewRuler.incomingContentForeground", A(blue, 0.6))
put("editorOverviewRuler.commonContentForeground", A(blue4, 0.6))
put("editorOverviewRuler.commentForeground", blue6)
put("editorOverviewRuler.commentUnresolvedForeground", orange)
put("editorOverviewRuler.inlineChatInserted", A(green, 0.5))
put("editorOverviewRuler.inlineChatRemoved", A(red, 0.5))

# widgets
put("editorWidget.background", bg_raise)
put("editorWidget.foreground", white3)
put("editorWidget.border", border)
put("editorWidget.resizeBorder", blue_vibrant)
put("editorActionList.background", bg_raise)
put("editorActionList.foreground", white3)
put("editorActionList.focusBackground", sel)
put("editorActionList.focusForeground", white)
put("editorSuggestWidget.background", bg_raise)
put("editorSuggestWidget.border", border)
put("editorSuggestWidget.foreground", white3)
put("editorSuggestWidget.focusHighlightForeground", orange3)
put("editorSuggestWidget.highlightForeground", orange3)
put("editorSuggestWidget.selectedBackground", sel)
put("editorSuggestWidget.selectedForeground", white)
put("editorSuggestWidget.selectedIconForeground", white)
put("editorSuggestWidgetStatus.foreground", blue6)
put("editorHoverWidget.background", bg_raise)
put("editorHoverWidget.foreground", white3)
put("editorHoverWidget.border", border)
put("editorHoverWidget.highlightForeground", orange3)
put("editorHoverWidget.statusBarBackground", bg_raise2)
put("debugExceptionWidget.background", hsl(357, 40, 22))
put("debugExceptionWidget.border", red)
put("editorMarkerNavigation.background", bg_raise)
put("editorMarkerNavigationError.background", red)
put("editorMarkerNavigationError.headerBackground", A(red, 0.1))
put("editorMarkerNavigationWarning.background", orange)
put("editorMarkerNavigationWarning.headerBackground", A(orange, 0.1))
put("editorMarkerNavigationInfo.background", blue)
put("editorMarkerNavigationInfo.headerBackground", A(blue, 0.1))

# peek view
put("peekView.border", blue5)
put("peekViewEditor.background", bg_side)
put("peekViewEditor.matchHighlightBackground", A(orange3, 0.4))
put("peekViewEditor.matchHighlightBorder", transparent)
put("peekViewEditorGutter.background", bg_side)
put("peekViewEditorStickyScroll.background", bg_side)
put("peekViewEditorStickyScrollGutter.background", bg_side)
put("peekViewResult.background", bg_deep)
put("peekViewResult.fileForeground", white3)
put("peekViewResult.lineForeground", blue6)
put("peekViewResult.matchHighlightBackground", A(orange3, 0.4))
put("peekViewResult.selectionBackground", sel)
put("peekViewResult.selectionForeground", white)
put("peekViewTitle.background", bg_raise)
put("peekViewTitleLabel.foreground", white)
put("peekViewTitleDescription.foreground", blue6)

# diff editor
put("diffEditor.insertedTextBackground", A(hsl(180, 60, 60), 0.30))
put("diffEditor.insertedTextBorder", transparent)
put("diffEditor.removedTextBackground", A(hsl(357, 60, 60), 0.30))
put("diffEditor.removedTextBorder", transparent)
put("diffEditor.insertedLineBackground", A(hsl(180, 45, 60), 0.15))
put("diffEditor.removedLineBackground", A(hsl(357, 45, 60), 0.15))
put("diffEditor.border", border)
put("diffEditor.diagonalFill", A(blue4, 0.4))
put("diffEditor.unchangedRegionBackground", bg_deep)
put("diffEditor.unchangedRegionForeground", blue6)
put("diffEditor.unchangedRegionShadow", A(black, 0.25))
put("diffEditor.unchangedCodeBackground", A(blue2, 0.15))
put("diffEditor.move.border", A(blue, 0.6))
put("diffEditor.moveActive.border", orange)
put("diffEditorGutter.insertedLineBackground", A(hsl(180, 60, 60), 0.25))
put("diffEditorGutter.removedLineBackground", A(hsl(357, 60, 60), 0.25))
put("diffEditorOverview.insertedForeground", A(hsl(180, 60, 60), 0.6))
put("diffEditorOverview.removedForeground", A(hsl(357, 60, 60), 0.6))
put("multiDiffEditor.headerBackground", bg_raise)
put("multiDiffEditor.background", bg)
put("multiDiffEditor.border", border)

# merge conflicts
put("merge.currentHeaderBackground", A(green, 0.35))
put("merge.currentContentBackground", A(green, 0.15))
put("merge.incomingHeaderBackground", A(blue, 0.35))
put("merge.incomingContentBackground", A(blue, 0.15))
put("merge.commonHeaderBackground", A(blue4, 0.35))
put("merge.commonContentBackground", A(blue4, 0.15))
put("merge.border", transparent)
put("mergeEditor.change.background", A(hsl(180, 45, 60), 0.15))
put("mergeEditor.change.word.background", A(hsl(180, 60, 60), 0.3))
put("mergeEditor.changeBase.background", A(hsl(357, 45, 60), 0.15))
put("mergeEditor.changeBase.word.background", A(hsl(357, 60, 60), 0.3))
put("mergeEditor.conflict.handled.minimapOverViewRuler", green)
put("mergeEditor.conflict.handledFocused.border", A(green, 0.8))
put("mergeEditor.conflict.handledUnfocused.border", A(green, 0.4))
put("mergeEditor.conflict.unhandled.minimapOverViewRuler", orange)
put("mergeEditor.conflict.unhandledFocused.border", orange)
put("mergeEditor.conflict.unhandledUnfocused.border", A(orange, 0.5))
put("mergeEditor.conflictingLines.background", A(orange, 0.15))

# ---------------------------------------------------------------- panel / output
put("panel.background", bg_side)
put("panel.border", border)
put("panel.dropBorder", white3)
put("panelTitle.activeBorder", blue5)
put("panelTitle.activeForeground", white)
put("panelTitle.inactiveForeground", dim)
put("panelTitle.border", border)
put("panelTitleBadge.background", blue_vibrant)
put("panelTitleBadge.foreground", bg_deeper)
put("panelInput.border", border)
put("panelSection.border", border)
put("panelSection.dropBackground", A(blue_vibrant, 0.25))
put("panelSectionHeader.background", bg_deep)
put("panelSectionHeader.foreground", white3)
put("panelSectionHeader.border", border)
put("panelStickyScroll.background", bg_side)
put("panelStickyScroll.border", border)
put("panelStickyScroll.shadow", A(black, 0.25))
put("outputView.background", bg_side)
put("outputViewStickyScroll.background", bg_side)

# ---------------------------------------------------------------- status bar / title bar / menus
put("statusBar.background", bg_deep)
put("statusBar.foreground", blue6)
put("statusBar.border", border)
put("statusBar.focusBorder", blue_vibrant)
put("statusBar.debuggingBackground", orange2)
put("statusBar.debuggingForeground", bg_deeper)
put("statusBar.debuggingBorder", border)
put("statusBar.noFolderBackground", bg_deep)
put("statusBar.noFolderForeground", blue6)
put("statusBar.noFolderBorder", border)
put("statusBarItem.activeBackground", A(white, 0.18))
put("statusBarItem.hoverBackground", A(white, 0.1))
put("statusBarItem.hoverForeground", white)
put("statusBarItem.focusBorder", blue_vibrant)
put("statusBarItem.compactHoverBackground", A(white, 0.2))
put("statusBarItem.prominentBackground", bg_raise2)
put("statusBarItem.prominentForeground", white3)
put("statusBarItem.prominentHoverBackground", hsl(210, 15, 36))
put("statusBarItem.prominentHoverForeground", white)
put("statusBarItem.remoteBackground", blue_vibrant)
put("statusBarItem.remoteForeground", bg_deeper)
put("statusBarItem.remoteHoverBackground", blue_br)
put("statusBarItem.remoteHoverForeground", bg_deeper)
put("statusBarItem.offlineBackground", red2)
put("statusBarItem.offlineForeground", bg_deeper)
put("statusBarItem.offlineHoverBackground", red)
put("statusBarItem.offlineHoverForeground", bg_deeper)
put("statusBarItem.errorBackground", red)
put("statusBarItem.errorForeground", bg_deeper)
put("statusBarItem.errorHoverBackground", red_br)
put("statusBarItem.errorHoverForeground", bg_deeper)
put("statusBarItem.warningBackground", orange2)
put("statusBarItem.warningForeground", bg_deeper)
put("statusBarItem.warningHoverBackground", orange)
put("statusBarItem.warningHoverForeground", bg_deeper)
put("titleBar.activeBackground", bg_deep)
put("titleBar.activeForeground", white3)
put("titleBar.inactiveBackground", bg_deep)
put("titleBar.inactiveForeground", blue4)
put("titleBar.border", border)
put("menubar.selectionForeground", white)
put("menubar.selectionBackground", A(blue2, 0.7))
put("menubar.selectionBorder", transparent)
put("menu.foreground", white3)
put("menu.background", bg_raise)
put("menu.selectionForeground", white)
put("menu.selectionBackground", sel)
put("menu.selectionBorder", transparent)
put("menu.separatorBackground", border)
put("menu.border", border)
put("commandCenter.foreground", blue6)
put("commandCenter.activeForeground", white)
put("commandCenter.background", bg)
put("commandCenter.activeBackground", bg_raise)
put("commandCenter.border", border)
put("commandCenter.inactiveForeground", blue4)
put("commandCenter.inactiveBorder", border)
put("commandCenter.activeBorder", blue4)
put("commandCenter.debuggingBackground", A(orange2, 0.3))

# ---------------------------------------------------------------- notifications / banner / quick input
put("notificationCenter.border", border)
put("notificationCenterHeader.foreground", white3)
put("notificationCenterHeader.background", bg_raise2)
put("notificationToast.border", border)
put("notifications.foreground", white3)
put("notifications.background", bg_raise)
put("notifications.border", border)
put("notificationLink.foreground", blue)
put("notificationsErrorIcon.foreground", red)
put("notificationsWarningIcon.foreground", orange)
put("notificationsInfoIcon.foreground", blue)
put("banner.background", bg_raise2)
put("banner.foreground", white3)
put("banner.iconForeground", blue)
put("pickerGroup.border", border)
put("pickerGroup.foreground", blue5)
put("quickInput.background", bg_raise)
put("quickInput.foreground", white3)
put("quickInputList.focusBackground", sel)
put("quickInputList.focusForeground", white)
put("quickInputList.focusIconForeground", white)
put("quickInputTitle.background", bg_raise2)

# ---------------------------------------------------------------- extensions / welcome / settings / breadcrumbs
put("extensionButton.background", blue_vibrant)
put("extensionButton.foreground", bg_deeper)
put("extensionButton.hoverBackground", blue_br)
put("extensionButton.separator", A(bg_deeper, 0.4))
put("extensionButton.prominentBackground", blue_vibrant)
put("extensionButton.prominentForeground", bg_deeper)
put("extensionButton.prominentHoverBackground", blue_br)
put("extensionIcon.starForeground", orange3)
put("extensionIcon.verifiedForeground", blue)
put("extensionIcon.preReleaseForeground", orange)
put("extensionIcon.sponsorForeground", pink)
put("welcomePage.background", bg)
put("welcomePage.progress.background", bg_deep)
put("welcomePage.progress.foreground", blue_vibrant)
put("welcomePage.tileBackground", bg_raise)
put("welcomePage.tileHoverBackground", bg_raise2)
put("welcomePage.tileBorder", border)
put("walkThrough.embeddedEditorBackground", bg_side)
put("walkthrough.stepTitle.foreground", white)
put("settings.headerForeground", white)
put("settings.headerBorder", border)
put("settings.sashBorder", border)
put("settings.modifiedItemIndicator", blue5)
put("settings.dropdownBackground", bg_deep)
put("settings.dropdownForeground", white3)
put("settings.dropdownBorder", border)
put("settings.dropdownListBorder", border)
put("settings.checkboxBackground", bg_deep)
put("settings.checkboxForeground", white3)
put("settings.checkboxBorder", blue4)
put("settings.rowHoverBackground", A(blue2, 0.25))
put("settings.focusedRowBackground", A(blue2, 0.35))
put("settings.focusedRowBorder", blue_vibrant)
put("settings.textInputBackground", bg_deep)
put("settings.textInputForeground", white3)
put("settings.textInputBorder", border)
put("settings.numberInputBackground", bg_deep)
put("settings.numberInputForeground", white3)
put("settings.numberInputBorder", border)
put("breadcrumb.foreground", blue6)
put("breadcrumb.background", bg)
put("breadcrumb.focusForeground", white)
put("breadcrumb.activeSelectionForeground", white)
put("breadcrumbPicker.background", bg_raise)
put("search.resultsInfoForeground", blue6)
put("searchEditor.findMatchBackground", A(orange3, 0.35))
put("searchEditor.findMatchBorder", transparent)
put("searchEditor.textInputBorder", border)
put("interactive.activeCodeBorder", blue5)
put("interactive.inactiveCodeBorder", border)
put("ports.iconRunningProcessForeground", green)
put("charts.foreground", white3)
put("charts.lines", blue6)
put("charts.red", red)
put("charts.blue", blue)
put("charts.yellow", orange3)
put("charts.orange", orange)
put("charts.green", green)
put("charts.purple", pink)

# ---------------------------------------------------------------- terminal
put("terminal.background", bg_side)
put("terminal.foreground", white3)
put("terminal.border", border)
put("terminal.selectionBackground", sel)
put("terminal.selectionForeground", white)
put("terminal.inactiveSelectionBackground", A(blue2, 0.5))
put("terminal.findMatchBackground", orange3)
put("terminal.findMatchBorder", orange3)
put("terminal.findMatchHighlightBackground", A(orange3, 0.35))
put("terminal.findMatchHighlightBorder", transparent)
put("terminal.hoverHighlightBackground", A(blue2, 0.5))
put("terminal.dropBackground", A(blue_vibrant, 0.25))
put("terminal.tab.activeBorder", blue5)
put("terminal.initialHintForeground", blue4)
put("terminalCursor.foreground", orange)
put("terminalCursor.background", bg_side)
put("terminalCommandDecoration.defaultBackground", blue4)
put("terminalCommandDecoration.successBackground", green)
put("terminalCommandDecoration.errorBackground", red)
put("terminalCommandGuide.foreground", A(blue5, 0.5))
put("terminalOverviewRuler.cursorForeground", A(orange, 0.7))
put("terminalOverviewRuler.findMatchForeground", A(orange3, 0.8))
put("terminalOverviewRuler.border", transparent)
put("terminalStickyScroll.background", bg_side)
put("terminalStickyScroll.border", border)
put("terminalStickyScrollHover.background", bg_raise)
put("terminal.ansiBlack", hsl(210, 15, 16))
put("terminal.ansiRed", red)
put("terminal.ansiGreen", green)
put("terminal.ansiYellow", orange3)
put("terminal.ansiBlue", blue)
put("terminal.ansiMagenta", pink)
put("terminal.ansiCyan", blue5)
put("terminal.ansiWhite", white3)
put("terminal.ansiBrightBlack", blue4)
put("terminal.ansiBrightRed", red_br)
put("terminal.ansiBrightGreen", green_br)
put("terminal.ansiBrightYellow", orange)
put("terminal.ansiBrightBlue", blue_br)
put("terminal.ansiBrightMagenta", pink_br)
put("terminal.ansiBrightCyan", cyan_br)
put("terminal.ansiBrightWhite", white)

# ---------------------------------------------------------------- debug
put("debugToolBar.background", bg_raise2)
put("debugToolBar.border", border)
put("debugIcon.breakpointForeground", red)
put("debugIcon.breakpointDisabledForeground", blue4)
put("debugIcon.breakpointUnverifiedForeground", orange2)
put("debugIcon.breakpointCurrentStackframeForeground", orange3)
put("debugIcon.breakpointStackframeForeground", green)
put("debugIcon.startForeground", green)
put("debugIcon.pauseForeground", blue)
put("debugIcon.stopForeground", red)
put("debugIcon.disconnectForeground", red)
put("debugIcon.restartForeground", green)
put("debugIcon.stepOverForeground", blue)
put("debugIcon.stepIntoForeground", blue)
put("debugIcon.stepOutForeground", blue)
put("debugIcon.continueForeground", blue)
put("debugIcon.stepBackForeground", blue)
put("debugConsole.infoForeground", blue)
put("debugConsole.warningForeground", orange)
put("debugConsole.errorForeground", red)
put("debugConsole.sourceForeground", blue6)
put("debugConsoleInputIcon.foreground", blue5)
put("debugTokenExpression.name", blue5)
put("debugTokenExpression.value", white3)
put("debugTokenExpression.string", green)
put("debugTokenExpression.boolean", red)
put("debugTokenExpression.number", orange)
put("debugTokenExpression.error", red)
put("debugView.exceptionLabelForeground", white3)
put("debugView.exceptionLabelBackground", hsl(357, 45, 35))
put("debugView.stateLabelForeground", blue6)
put("debugView.stateLabelBackground", bg_raise2)
put("debugView.valueChangedHighlight", orange3)

# ---------------------------------------------------------------- testing
put("testing.iconFailed", red)
put("testing.iconErrored", red2)
put("testing.iconPassed", green)
put("testing.runAction", green)
put("testing.iconQueued", orange)
put("testing.iconUnset", blue4)
put("testing.iconSkipped", blue4)
put("testing.peekBorder", red)
put("testing.peekHeaderBackground", A(red, 0.1))
put("testing.message.error.badgeBackground", red)
put("testing.message.error.badgeBorder", red)
put("testing.message.error.badgeForeground", bg_deeper)
put("testing.message.error.lineBackground", A(red, 0.15))
put("testing.message.info.decorationForeground", A(white3, 0.5))
put("testing.message.info.lineBackground", A(blue, 0.15))
put("testing.coveredBackground", A(green, 0.2))
put("testing.coveredBorder", A(green, 0.4))
put("testing.coveredGutterBackground", A(green, 0.35))
put("testing.uncoveredBranchBackground", A(orange, 0.25))
put("testing.uncoveredBackground", A(red, 0.2))
put("testing.uncoveredBorder", A(red, 0.4))
put("testing.uncoveredGutterBackground", A(red, 0.35))
put("testing.coverCountBadgeBackground", blue_vibrant)
put("testing.coverCountBadgeForeground", bg_deeper)

# ---------------------------------------------------------------- git / scm
put("gitDecoration.addedResourceForeground", green)
put("gitDecoration.modifiedResourceForeground", orange)
put("gitDecoration.deletedResourceForeground", red)
put("gitDecoration.renamedResourceForeground", blue5)
put("gitDecoration.stageModifiedResourceForeground", orange)
put("gitDecoration.stageDeletedResourceForeground", red)
put("gitDecoration.untrackedResourceForeground", green)
put("gitDecoration.ignoredResourceForeground", blue4)
put("gitDecoration.conflictingResourceForeground", red2)
put("gitDecoration.submoduleResourceForeground", pink)
for i, col in enumerate([blue, orange, pink, green, blue5], 1):
    put("scmGraph.foreground%d" % i, col)
put("scmGraph.historyItemRefColor", blue)
put("scmGraph.historyItemRemoteRefColor", pink)
put("scmGraph.historyItemBaseRefColor", orange)
put("scmGraph.historyItemHoverDefaultLabelBackground", bg_raise2)
put("scmGraph.historyItemHoverDefaultLabelForeground", white3)
put("scmGraph.historyItemHoverLabelForeground", bg_deeper)
put("scmGraph.historyItemHoverAdditionsForeground", green)
put("scmGraph.historyItemHoverDeletionsForeground", red)

# ---------------------------------------------------------------- notebooks
put("notebook.editorBackground", bg)
put("notebook.cellBorderColor", A(blue4, 0.4))
put("notebook.cellEditorBackground", bg_side)
put("notebook.cellHoverBackground", A(blue2, 0.2))
put("notebook.cellInsertionIndicator", blue_vibrant)
put("notebook.cellStatusBarItemHoverBackground", A(blue2, 0.5))
put("notebook.cellToolbarSeparator", A(blue4, 0.4))
put("notebook.focusedCellBackground", A(blue2, 0.2))
put("notebook.focusedCellBorder", blue_vibrant)
put("notebook.focusedEditorBorder", blue_vibrant)
put("notebook.inactiveFocusedCellBorder", A(blue4, 0.6))
put("notebook.inactiveSelectedCellBorder", A(blue4, 0.6))
put("notebook.outputContainerBackgroundColor", bg_side)
put("notebook.outputContainerBorderColor", A(blue4, 0.4))
put("notebook.selectedCellBackground", A(blue2, 0.3))
put("notebook.selectedCellBorder", A(blue4, 0.6))
put("notebook.symbolHighlightBackground", A(blue5, 0.25))
put("notebookScrollbarSlider.background", A(blue4, 0.35))
put("notebookScrollbarSlider.hoverBackground", A(blue4, 0.55))
put("notebookScrollbarSlider.activeBackground", A(blue4, 0.75))
put("notebookStatusErrorIcon.foreground", red)
put("notebookStatusRunningIcon.foreground", blue6)
put("notebookStatusSuccessIcon.foreground", green)
put("notebookEditorOverviewRuler.runningCellForeground", green)

# ---------------------------------------------------------------- AI / chat
put("chat.requestBorder", border)
put("chat.requestBackground", bg_side)
put("chat.slashCommandBackground", A(blue_vibrant, 0.25))
put("chat.slashCommandForeground", blue)
put("chat.avatarBackground", bg_raise2)
put("chat.avatarForeground", white3)
put("chat.editedFileForeground", orange)
put("chat.linesAddedForeground", green)
put("chat.linesRemovedForeground", red)
put("inlineChat.background", bg_raise)
put("inlineChat.foreground", white3)
put("inlineChat.border", border)
put("inlineChat.shadow", A(black, 0.25))
put("inlineChat.regionHighlight", A(blue2, 0.4))
put("inlineChatInput.background", bg_deep)
put("inlineChatInput.border", border)
put("inlineChatInput.focusBorder", blue_vibrant)
put("inlineChatInput.placeholderForeground", blue4)
put("inlineChatDiff.inserted", A(hsl(180, 45, 60), 0.15))
put("inlineChatDiff.removed", A(hsl(357, 45, 60), 0.15))
put("editorOverviewRuler.inlineChatInserted", A(green, 0.5))
put("editorOverviewRuler.inlineChatRemoved", A(red, 0.5))
put("minimapGutter.inlineChatInserted", green)
put("minimapGutter.inlineChatRemoved", red)

# ---------------------------------------------------------------- symbol icons
sym = {
    "array": blue5, "boolean": red, "class": orange, "color": pink,
    "constant": pink, "constructor": blue5, "enumerator": orange,
    "enumeratorMember": pink, "event": orange, "field": red, "file": blue6,
    "folder": blue6, "function": blue5, "interface": orange, "key": blue5,
    "keyword": pink, "method": blue5, "module": orange, "namespace": orange,
    "null": red, "number": orange, "object": orange, "operator": red2,
    "package": orange, "property": red, "reference": blue, "snippet": blue6,
    "string": green, "struct": orange, "text": white3, "typeParameter": orange,
    "unit": orange, "variable": white3,
}
for name, col in sym.items():
    put("symbolIcon.%sForeground" % name, col)

# ---------------------------------------------------------------- newer / secondary keys
put("actionBar.toggledBackground", A(blue_vibrant, 0.35))
put("button.secondaryBorder", transparent)
put("editor.inactiveLineHighlightBackground", A(blue2, 0.15))
put("editorGroupHeader.connectedTabsBackground", bg_deep)
put("editorIndentGuide.activeBackground", A(blue5, 0.7))
put("editorIndentGuide.background", A(blue5, 0.2))
put("editorGutter.addedSecondaryBackground", A(green, 0.5))
put("editorGutter.modifiedSecondaryBackground", A(orange, 0.5))
put("editorGutter.deletedSecondaryBackground", A(red, 0.5))
put("editorGutter.itemBackground", bg_raise)
put("editorGutter.itemGlyphForeground", white3)
put("editorGutter.commentGlyphForeground", blue6)
put("editorGutter.commentUnresolvedGlyphForeground", orange)
put("editorGutter.commentDraftGlyphForeground", blue4)
put("editorOverviewRuler.commentDraftForeground", blue4)
put("editorSuggestWidget.focusOutline", blue_vibrant)
put("extensionIcon.privateForeground", blue4)
put("mcpIcon.starForeground", orange3)
put("mergeEditor.acceptInput1", A(green, 0.3))
put("mergeEditor.acceptInput2", A(blue, 0.3))
put("profiles.sashBorder", border)
put("quickInput.list.focusBackground", sel)
put("quickInputList.focusHighlightForeground", orange3)
put("scm.historyItemAdditionsForeground", green)
put("scm.historyItemDeletionsForeground", red)
put("scm.historyItemStatisticsBorder", A(blue4, 0.4))
put("scm.historyItemSelectedStatisticsBorder", blue_vibrant)
put("settings.settingsHeaderHoverForeground", white)
put("sideBySideEditor.horizontalBorder", border)
put("sideBySideEditor.verticalBorder", border)
put("simpleFindWidget.sashBorder", border)
put("statusBar.inactiveBackground", bg_deep)
put("tab.dragAndDropBorder", blue_vibrant)
put("terminal.integrated.tabs.defaultColor", blue6)
put("testing.coveredMinimapBackground", A(green, 0.5))
put("testing.uncoveredMinimapBackground", A(red, 0.5))
put("testing.messagePeekBorder", red)
put("testing.messagePeekHeaderBackground", A(red, 0.1))
put("chat.checkpointSeparator", blue4)
put("chat.findMatchBackground", A(orange3, 0.6))
put("chat.findMatchHighlightBackground", A(orange3, 0.3))
put("chat.requestBubbleBackground", A(blue2, 0.4))
put("chat.requestBubbleHoverBackground", A(blue2, 0.6))
put("chat.requestCodeBorder", border)
put("chat.statusBackground", bg_raise)
put("chat.mcpCompatibilityWarningForeground", orange)
put("chat.sessionStateIndicator.inProgressBorder", blue5)
put("chat.sessionStateIndicator.needsInputBorder", orange)
put("chat.sessionStateIndicator.unvisitedBorder", blue_vibrant)
put("chat.inputWorkingBorderColor1", blue5)
put("chat.inputWorkingBorderColor2", blue_vibrant)
put("chat.inputWorkingBorderColor3", pink)
put("chat.voiceGlowBaseColor", blue_vibrant)
put("chat.workingProgressStableIconForeground", blue5)
put("chat.workingProgressInsidersIconForeground", green)
put("agentsChatInput.focusBorder", blue_vibrant)
put("agentsChatInput.placeholderForeground", blue4)
put("agentsGradient.tintColor", blue_vibrant)
put("agentsNewSessionButton.hoverBackground", blue_br)
put("agentsUpdateButton.downloadedBackground", green)
put("agentsUpdateButton.downloadingBackground", orange)
put("agentsVoice.speakingBackground", A(blue_vibrant, 0.3))
put("agentsVoice.speakingForeground", white3)
put("inlineEdit.gutterIndicator.primaryBackground", A(blue_vibrant, 0.4))
put("inlineEdit.gutterIndicator.primaryBorder", blue_vibrant)
put("inlineEdit.gutterIndicator.primaryForeground", white)
put("inlineEdit.gutterIndicator.secondaryBackground", bg_raise2)
put("inlineEdit.gutterIndicator.secondaryBorder", blue4)
put("inlineEdit.gutterIndicator.secondaryForeground", white3)
put("inlineEdit.gutterIndicator.successfulBackground", A(green, 0.4))
put("inlineEdit.gutterIndicator.successfulBorder", green)
put("inlineEdit.gutterIndicator.successfulForeground", white)
put("inlineEdit.modifiedBackground", A(hsl(180, 45, 60), 0.15))
put("inlineEdit.modifiedBorder", A(hsl(180, 45, 60), 0.5))
put("inlineEdit.modifiedChangedLineBackground", A(hsl(180, 45, 60), 0.15))
put("inlineEdit.modifiedChangedTextBackground", A(hsl(180, 60, 60), 0.3))
put("inlineEdit.originalBackground", A(hsl(357, 45, 60), 0.15))
put("inlineEdit.originalBorder", A(hsl(357, 45, 60), 0.5))
put("inlineEdit.originalChangedLineBackground", A(hsl(357, 45, 60), 0.15))
put("inlineEdit.originalChangedTextBackground", A(hsl(357, 60, 60), 0.3))
put("inlineEdit.tabWillAcceptModifiedBorder", blue5)
put("inlineEdit.tabWillAcceptOriginalBorder", blue5)
put("modernActivityBar.activeBackground", transparent)
put("modernActivityBar.activeForeground", white)
put("modernActivityBar.hoverBackground", A(blue2, 0.4))
put("modernActivityBar.hoverForeground", white)
put("modernActivityBar.inactiveBackground", transparent)
put("modernActivityBarItem.activeBackground", A(blue2, 0.7))
put("modernActivityBarItem.activeForeground", white)
put("modernActivityBarItem.hoverBackground", A(blue2, 0.4))
put("modernActivityBarItem.hoverForeground", white)
put("modernEditorTab.activeActionBackground", A(blue2, 0.4))
put("modernEditorTab.activeBackground", bg)
put("modernEditorTab.activeForeground", white)
put("modernEditorTab.activeHoverActionBackground", A(blue2, 0.6))
put("modernEditorTab.activeHoverBackground", bg_raise)
put("modernEditorTab.hoverActionBackground", A(blue2, 0.4))
put("modernEditorTab.hoverBackground", bg_raise)
put("modernEditorTab.hoverForeground", white)
put("modernEditorTab.inactiveBackground", bg_deep)
put("modernEditorTab.selectedActionBackground", A(blue2, 0.4))
put("modernSash.gripForeground", blue4)
put("modernTab.activeBackground", bg)
put("modernTab.activeForeground", white)
put("modernTab.hoverBackground", bg_raise)
put("modernTab.hoverForeground", white)
put("modernUI.inactiveShellBackground", bg_deep)
put("modernUI.shellBackground", bg_deep)
for name, col in {
    "alias": blue5, "argument": orange, "branch": pink, "commit": blue,
    "file": blue6, "flag": pink, "folder": blue6, "inlineSuggestion": blue4,
    "method": blue5, "option": pink, "optionValue": orange,
    "pullRequest": green, "pullRequestDone": pink, "remote": blue,
    "stash": orange, "symbolicLinkFile": blue6, "symbolicLinkFolder": blue6,
    "tag": orange3,
}.items():
    put("terminalSymbolIcon.%sForeground" % name, col)

# ---------------------------------------------------------------- token colors
def tok(scope, fg=None, style=None, name=None):
    settings = {}
    if fg:
        settings["foreground"] = fg
    if style:
        settings["fontStyle"] = style
    r = {"scope": scope, "settings": settings}
    if name:
        r["name"] = name
    return r


T = [
    tok("comment, punctuation.definition.comment", blue6, name="Comment"),
    tok("string", green, name="String"),
    tok("punctuation.definition", blue5, name="Punctuation"),
    tok("punctuation.definition.numeric.base", orange),
    tok("constant.numeric", orange, name="Number"),
    tok("keyword.other.unit, storage.type.numeric", pink, "italic", "Number suffix / unit"),
    tok("constant.language", red, "italic", "Built-in constant"),
    tok("constant.character, constant.other, constant.character.escape", pink, name="User-defined constant"),
    tok("variable.other.member, variable.other.property, variable.other.object.property, meta.object-literal.key, support.variable.property", red, name="Member variable"),
    tok("keyword, keyword.control, keyword.operator.new, keyword.operator.expression, keyword.operator.word, keyword.operator.logical.python, keyword.operator.wordlike, keyword.other", pink, name="Keyword"),
    tok("keyword.operator, keyword.operator.assignment, keyword.operator.arithmetic, keyword.operator.comparison, keyword.operator.logical, keyword.operator.relational, keyword.operator.ternary, keyword.operator.type", red2, name="Operators"),
    tok("punctuation.separator, punctuation.terminator, punctuation.accessor, punctuation.separator.comma, punctuation.separator.key-value", blue6, name="Separators"),
    tok("punctuation.section, punctuation.definition.block, punctuation.definition.parameters, punctuation.definition.arguments, punctuation.definition.array, punctuation.definition.dictionary, punctuation.definition.binding-pattern, punctuation.definition.template-expression, punctuation.section.embedded, meta.brace, meta.delimiter", white, name="Section punctuation"),
    tok("punctuation.definition.annotation, punctuation.decorator, punctuation.definition.decorator", blue5, name="Annotation punctuation"),
    tok("storage, storage.modifier", red, name="Storage"),
    tok("storage.type, storage.type.function, storage.type.class, storage.type.js, storage.type.ts, storage.type.interface", pink, "italic", "Storage type"),
    tok("entity.name.function, support.function.definition, meta.definition.function entity.name.function, meta.definition.method entity.name.function", blue5, name="Function definition"),
    tok("entity.name.class, entity.name.type, entity.name.namespace, entity.name.module, entity.name.struct, entity.name.enum, entity.name.interface, entity.name.trait, entity.name.type.class, entity.name.type.module, entity.name.type.interface, entity.name.type.enum, entity.name.type.struct, entity.name.type.parameter, entity.name.package, entity.name.variable, entity.name.constant", orange, name="Entity name"),
    tok("entity.other.inherited-class", blue5, "italic", "Inherited class"),
    tok("variable.parameter, meta.function.parameters variable, variable.parameter.function", orange, name="Function argument"),
    tok("variable.language, variable.language.this, variable.language.self, variable.language.super", red, "italic", "Language variable"),
    tok("entity.name.tag, meta.tag entity.name, entity.name.tag.html", red, name="Tag name"),
    tok("entity.other.attribute-name, entity.other.attribute-name.html, entity.other.attribute-name.class.css, entity.other.attribute-name.id.css", pink, name="Tag attribute"),
    tok("meta.function-call entity.name.function, meta.function-call.generic, meta.method-call entity.name.function, variable.function, entity.name.function.call, meta.function-call support.function, entity.name.function.decorator, meta.decorator variable.other.readwrite, meta.annotation, variable.annotation", blue, name="Function call"),
    tok("support.function, support.macro, support.function.builtin, support.function.magic", blue, "italic", "Library function"),
    tok("support.constant", pink, "italic", "Library constant"),
    tok("support.type, support.class, support.type.primitive, support.type.builtin, support.other.namespace", blue, "italic", "Library class/type"),
    tok("invalid", red, name="Invalid"),
    tok("invalid.deprecated", orange2, name="Invalid deprecated"),
    tok("entity.name.tag.yaml", blue5, name="YAML key"),
    tok("source.yaml string.unquoted", white3, name="YAML string"),
    tok("support.type.property-name, support.type.property-name.json, support.type.property-name.css, meta.property-name", white3, name="CSS / JSON property"),
    tok("markup.heading, entity.name.section.markdown, markup.heading.setext", None, "bold", "Markup headings"),
    tok("punctuation.definition.heading, beginning.punctuation.definition.heading", red2, name="Heading punctuation"),
    tok("markup.heading.1 punctuation.definition.heading, markup.heading.1.markdown punctuation.definition.heading.markdown", red, name="h1 punctuation"),
    tok("string.other.link, markup.underline.link, string.other.link.title.markdown, string.other.link.description.markdown", blue, name="Links"),
    tok("markup.bold", None, "bold", "Bold"),
    tok("markup.italic", None, "italic", "Italic"),
    tok("markup.underline", None, "underline", "Underline"),
    tok("markup.bold markup.italic, markup.italic markup.bold", None, "bold italic", "Bold italic"),
    tok("punctuation.definition.thematic-break, meta.separator.markdown", orange, name="Horizontal rule"),
    tok("markup.list.numbered.bullet, beginning.punctuation.definition.list.markdown", green, name="Numbered list bullet"),
    tok("markup.quote punctuation.definition.blockquote, markup.list punctuation.definition.list_item, markup.list punctuation.definition.list.begin, punctuation.definition.quote.begin.markdown", orange, name="Blockquote / list bullet"),
    tok("markup.inline.raw, markup.raw, markup.fenced_code.block", white3, name="Inline code"),
    tok("punctuation.definition.italic, punctuation.definition.bold, punctuation.definition.bold.markdown, punctuation.definition.italic.markdown", pink, name="Emphasis punctuation"),
    tok("meta.diff, meta.diff.header, meta.separator.diff, meta.diff.range", pink, name="Diff header"),
    tok("markup.deleted, punctuation.definition.deleted", red, name="Diff deleted"),
    tok("markup.inserted, punctuation.definition.inserted", green, name="Diff inserted"),
    tok("markup.changed, punctuation.definition.changed", orange, name="Diff changed"),
    tok("constant.numeric.line-number.match", red),
    tok("message.error", red),
    tok("string.regexp", orange3, name="Regular expression"),
    tok("constant.other.color, constant.other.rgb-value", pink, name="Color value"),
    tok("support.type.vendored.property-name, support.type.property-name.variable.css", white3, name="CSS vendor property"),
    tok("entity.other.attribute-name.pseudo-class.css, entity.other.attribute-name.pseudo-element.css", blue5, name="CSS pseudo"),
    tok("entity.name.tag.css, entity.name.tag.reference.scss", red, name="CSS selector tag"),
    tok("meta.preprocessor, keyword.control.directive", pink, name="Preprocessor"),
    tok("keyword.control.import, keyword.control.export, keyword.control.from, keyword.control.as, keyword.control.default", pink, name="Import / export"),
    tok("variable.other.readwrite.alias, variable.other.constant.object", white3, name="Alias / constant object"),
]

semantic = {
    "namespace": orange,
    "type": orange,
    "class": orange,
    "enum": orange,
    "interface": orange,
    "struct": orange,
    "typeParameter": orange,
    "parameter": orange,
    "variable": white3,
    "property": red,
    "enumMember": pink,
    "function": blue,
    "function.declaration": blue5,
    "method": blue,
    "method.declaration": blue5,
    "macro": blue,
    "decorator": blue,
    "keyword": pink,
    "string": green,
    "number": orange,
    "regexp": orange3,
    "comment": blue6,
    "operator": red2,
    "event": orange,
    "label": orange,
    "variable.defaultLibrary": {"foreground": red, "fontStyle": "italic"},
    "function.defaultLibrary": {"foreground": blue, "fontStyle": "italic"},
    "method.defaultLibrary": {"foreground": blue, "fontStyle": "italic"},
    "class.defaultLibrary": {"foreground": blue, "fontStyle": "italic"},
    "type.defaultLibrary": {"foreground": blue, "fontStyle": "italic"},
    "variable.readonly": white3,
    "*.deprecated": {"strikethrough": True},
}

# keys that are not registered colors in current VS Code
for k in list(c):
    if k.startswith(("secondarySideBar", "scm.historyItem", "minimapGutter.inlineChat")) or k in (
        "editor.foldControlForeground",
        "editorGutter.commentGlyphsForeground",
        "editorGutter.commentUnresolvedGlyphsForeground",
        "inlineChat.regionHighlight",
    ):
        del c[k]

theme = {
    "$schema": "vscode://schemas/color-theme",
    "name": "Trench",
    "type": "dark",
    "semanticHighlighting": True,
    "colors": c,
    "tokenColors": T,
    "semanticTokenColors": semantic,
}

os.makedirs(os.path.join(OUT, "themes"), exist_ok=True)
with open(os.path.join(OUT, "themes", "Trench-color-theme.json"), "w") as f:
    json.dump(theme, f, indent=2)
    f.write("\n")
print("colors:", len(c), "token rules:", len(T))
