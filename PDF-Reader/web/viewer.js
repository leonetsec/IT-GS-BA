/* Copyright 2016 Mozilla Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { RenderingStates, ScrollMode, SpreadMode } from "./ui_utils.js";
import { AppOptions } from "./app_options.js";
import { LinkTarget } from "./pdf_link_service.js";
import { PDFViewerApplication } from "./app.js";

/* eslint-disable-next-line no-unused-vars */
const pdfjsVersion =
  typeof PDFJSDev !== "undefined" ? PDFJSDev.eval("BUNDLE_VERSION") : void 0;
/* eslint-disable-next-line no-unused-vars */
const pdfjsBuild =
  typeof PDFJSDev !== "undefined" ? PDFJSDev.eval("BUNDLE_BUILD") : void 0;

const AppConstants =
  typeof PDFJSDev === "undefined" || PDFJSDev.test("GENERIC")
    ? { LinkTarget, RenderingStates, ScrollMode, SpreadMode }
    : null;

window.PDFViewerApplication = PDFViewerApplication;
window.PDFViewerApplicationConstants = AppConstants;
window.PDFViewerApplicationOptions = AppOptions;

function getViewerConfiguration() {
  return {
    appContainer: document.body,
    principalContainer: document.getElementById("mainContainer"),
    mainContainer: document.getElementById("viewerContainer"),
    viewerContainer: document.getElementById("viewer"),
    toolbar: {
      container: document.getElementById("toolbarContainer"),
      numPages: document.getElementById("numPages"),
      pageNumber: document.getElementById("pageNumber"),
      scaleSelect: document.getElementById("scaleSelect"),
      customScaleOption: document.getElementById("customScaleOption"),
      previous: document.getElementById("previous"),
      next: document.getElementById("next"),
      zoomIn: document.getElementById("zoomInButton"),
      zoomOut: document.getElementById("zoomOutButton"),
      print: document.getElementById("printButton"),
      editorFreeTextButton: document.getElementById("editorFreeTextButton"),
      editorFreeTextParamsToolbar: document.getElementById(
        "editorFreeTextParamsToolbar"
      ),
      editorHighlightButton: document.getElementById("editorHighlightButton"),
      editorHighlightParamsToolbar: document.getElementById(
        "editorHighlightParamsToolbar"
      ),
      editorHighlightColorPicker: document.getElementById(
        "editorHighlightColorPicker"
      ),
      editorInkButton: document.getElementById("editorInkButton"),
      editorInkParamsToolbar: document.getElementById("editorInkParamsToolbar"),
      editorStampButton: document.getElementById("editorStampButton"),
      editorStampParamsToolbar: document.getElementById(
        "editorStampParamsToolbar"
      ),
      editorSignatureButton: document.getElementById("editorSignatureButton"),
      editorSignatureParamsToolbar: document.getElementById(
        "editorSignatureParamsToolbar"
      ),
      download: document.getElementById("downloadButton"),
    },
    secondaryToolbar: {
      toolbar: document.getElementById("secondaryToolbar"),
      toggleButton: document.getElementById("secondaryToolbarToggleButton"),
      presentationModeButton: document.getElementById("presentationMode"),
      openFileButton:
        typeof PDFJSDev === "undefined" || PDFJSDev.test("GENERIC")
          ? document.getElementById("secondaryOpenFile")
          : null,
      printButton: document.getElementById("secondaryPrint"),
      downloadButton: document.getElementById("secondaryDownload"),
      viewBookmarkButton: document.getElementById("viewBookmark"),
      firstPageButton: document.getElementById("firstPage"),
      lastPageButton: document.getElementById("lastPage"),
      pageRotateCwButton: document.getElementById("pageRotateCw"),
      pageRotateCcwButton: document.getElementById("pageRotateCcw"),
      cursorSelectToolButton: document.getElementById("cursorSelectTool"),
      cursorHandToolButton: document.getElementById("cursorHandTool"),
      scrollPageButton: document.getElementById("scrollPage"),
      scrollVerticalButton: document.getElementById("scrollVertical"),
      scrollHorizontalButton: document.getElementById("scrollHorizontal"),
      scrollWrappedButton: document.getElementById("scrollWrapped"),
      spreadNoneButton: document.getElementById("spreadNone"),
      spreadOddButton: document.getElementById("spreadOdd"),
      spreadEvenButton: document.getElementById("spreadEven"),
      imageAltTextSettingsButton: document.getElementById(
        "imageAltTextSettings"
      ),
      imageAltTextSettingsSeparator: document.getElementById(
        "imageAltTextSettingsSeparator"
      ),
      documentPropertiesButton: document.getElementById("documentProperties"),
    },
    sidebar: {
      // Divs (and sidebar button)
      outerContainer: document.getElementById("outerContainer"),
      sidebarContainer: document.getElementById("sidebarContainer"),
      toggleButton: document.getElementById("sidebarToggleButton"),
      resizer: document.getElementById("sidebarResizer"),
      // Buttons
      thumbnailButton: document.getElementById("viewThumbnail"),
      outlineButton: document.getElementById("viewOutline"),
      attachmentsButton: document.getElementById("viewAttachments"),
      layersButton: document.getElementById("viewLayers"),
      // Views
      thumbnailView: document.getElementById("thumbnailView"),
      outlineView: document.getElementById("outlineView"),
      attachmentsView: document.getElementById("attachmentsView"),
      layersView: document.getElementById("layersView"),
      // View-specific options
      currentOutlineItemButton: document.getElementById("currentOutlineItem"),
    },
    findBar: {
      bar: document.getElementById("findbar"),
      toggleButton: document.getElementById("viewFindButton"),
      findField: document.getElementById("findInput"),
      highlightAllCheckbox: document.getElementById("findHighlightAll"),
      caseSensitiveCheckbox: document.getElementById("findMatchCase"),
      matchDiacriticsCheckbox: document.getElementById("findMatchDiacritics"),
      entireWordCheckbox: document.getElementById("findEntireWord"),
      findMsg: document.getElementById("findMsg"),
      findResultsCount: document.getElementById("findResultsCount"),
      findPreviousButton: document.getElementById("findPreviousButton"),
      findNextButton: document.getElementById("findNextButton"),
    },
    passwordOverlay: {
      dialog: document.getElementById("passwordDialog"),
      label: document.getElementById("passwordText"),
      input: document.getElementById("password"),
      submitButton: document.getElementById("passwordSubmit"),
      cancelButton: document.getElementById("passwordCancel"),
    },
    documentProperties: {
      dialog: document.getElementById("documentPropertiesDialog"),
      closeButton: document.getElementById("documentPropertiesClose"),
      fields: {
        fileName: document.getElementById("fileNameField"),
        fileSize: document.getElementById("fileSizeField"),
        title: document.getElementById("titleField"),
        author: document.getElementById("authorField"),
        subject: document.getElementById("subjectField"),
        keywords: document.getElementById("keywordsField"),
        creationDate: document.getElementById("creationDateField"),
        modificationDate: document.getElementById("modificationDateField"),
        creator: document.getElementById("creatorField"),
        producer: document.getElementById("producerField"),
        version: document.getElementById("versionField"),
        pageCount: document.getElementById("pageCountField"),
        pageSize: document.getElementById("pageSizeField"),
        linearized: document.getElementById("linearizedField"),
      },
    },
    altTextDialog: {
      dialog: document.getElementById("altTextDialog"),
      optionDescription: document.getElementById("descriptionButton"),
      optionDecorative: document.getElementById("decorativeButton"),
      textarea: document.getElementById("descriptionTextarea"),
      cancelButton: document.getElementById("altTextCancel"),
      saveButton: document.getElementById("altTextSave"),
    },
    newAltTextDialog: {
      dialog: document.getElementById("newAltTextDialog"),
      title: document.getElementById("newAltTextTitle"),
      descriptionContainer: document.getElementById(
        "newAltTextDescriptionContainer"
      ),
      textarea: document.getElementById("newAltTextDescriptionTextarea"),
      disclaimer: document.getElementById("newAltTextDisclaimer"),
      learnMore: document.getElementById("newAltTextLearnMore"),
      imagePreview: document.getElementById("newAltTextImagePreview"),
      createAutomatically: document.getElementById(
        "newAltTextCreateAutomatically"
      ),
      createAutomaticallyButton: document.getElementById(
        "newAltTextCreateAutomaticallyButton"
      ),
      downloadModel: document.getElementById("newAltTextDownloadModel"),
      downloadModelDescription: document.getElementById(
        "newAltTextDownloadModelDescription"
      ),
      error: document.getElementById("newAltTextError"),
      errorCloseButton: document.getElementById("newAltTextCloseButton"),
      cancelButton: document.getElementById("newAltTextCancel"),
      notNowButton: document.getElementById("newAltTextNotNow"),
      saveButton: document.getElementById("newAltTextSave"),
    },
    altTextSettingsDialog: {
      dialog: document.getElementById("altTextSettingsDialog"),
      createModelButton: document.getElementById("createModelButton"),
      aiModelSettings: document.getElementById("aiModelSettings"),
      learnMore: document.getElementById("altTextSettingsLearnMore"),
      deleteModelButton: document.getElementById("deleteModelButton"),
      downloadModelButton: document.getElementById("downloadModelButton"),
      showAltTextDialogButton: document.getElementById(
        "showAltTextDialogButton"
      ),
      altTextSettingsCloseButton: document.getElementById(
        "altTextSettingsCloseButton"
      ),
      closeButton: document.getElementById("altTextSettingsCloseButton"),
    },
    addSignatureDialog: {
      dialog: document.getElementById("addSignatureDialog"),
      panels: document.getElementById("addSignatureActionContainer"),
      typeButton: document.getElementById("addSignatureTypeButton"),
      typeInput: document.getElementById("addSignatureTypeInput"),
      drawButton: document.getElementById("addSignatureDrawButton"),
      drawSVG: document.getElementById("addSignatureDraw"),
      drawPlaceholder: document.getElementById("addSignatureDrawPlaceholder"),
      drawThickness: document.getElementById("addSignatureDrawThickness"),
      imageButton: document.getElementById("addSignatureImageButton"),
      imageSVG: document.getElementById("addSignatureImage"),
      imagePlaceholder: document.getElementById("addSignatureImagePlaceholder"),
      imagePicker: document.getElementById("addSignatureFilePicker"),
      imagePickerLink: document.getElementById("addSignatureImageBrowse"),
      description: document.getElementById("addSignatureDescription"),
      clearButton: document.getElementById("clearSignatureButton"),
      saveContainer: document.getElementById("addSignatureSaveContainer"),
      saveCheckbox: document.getElementById("addSignatureSaveCheckbox"),
      errorBar: document.getElementById("addSignatureError"),
      errorCloseButton: document.getElementById("addSignatureErrorCloseButton"),
      cancelButton: document.getElementById("addSignatureCancelButton"),
      addButton: document.getElementById("addSignatureAddButton"),
    },
    editSignatureDialog: {
      dialog: document.getElementById("editSignatureDescriptionDialog"),
      description: document.getElementById("editSignatureDescription"),
      editSignatureView: document.getElementById("editSignatureView"),
      cancelButton: document.getElementById("editSignatureCancelButton"),
      updateButton: document.getElementById("editSignatureUpdateButton"),
    },
    annotationEditorParams: {
      editorFreeTextFontSize: document.getElementById("editorFreeTextFontSize"),
      editorFreeTextColor: document.getElementById("editorFreeTextColor"),
      editorInkColor: document.getElementById("editorInkColor"),
      editorInkThickness: document.getElementById("editorInkThickness"),
      editorInkOpacity: document.getElementById("editorInkOpacity"),
      editorStampAddImage: document.getElementById("editorStampAddImage"),
      editorSignatureAddSignature: document.getElementById(
        "editorSignatureAddSignature"
      ),
      editorFreeHighlightThickness: document.getElementById(
        "editorFreeHighlightThickness"
      ),
      editorHighlightShowAll: document.getElementById("editorHighlightShowAll"),
    },
    printContainer: document.getElementById("printContainer"),
    editorUndoBar: {
      container: document.getElementById("editorUndoBar"),
      message: document.getElementById("editorUndoBarMessage"),
      undoButton: document.getElementById("editorUndoBarUndoButton"),
      closeButton: document.getElementById("editorUndoBarCloseButton"),
    },
  };
}

function webViewerLoad() {
  const config = getViewerConfiguration();

  if (typeof PDFJSDev !== "undefined" && PDFJSDev.test("GENERIC")) {
    // Give custom implementations of the default viewer a simpler way to
    // set various `AppOptions`, by dispatching an event once all viewer
    // files are loaded but *before* the viewer initialization has run.
    const event = new CustomEvent("webviewerloaded", {
      bubbles: true,
      cancelable: true,
      detail: {
        source: window,
      },
    });
    try {
      // Attempt to dispatch the event at the embedding `document`,
      // in order to support cases where the viewer is embedded in
      // a *dynamically* created <iframe> element.
      parent.document.dispatchEvent(event);
    } catch (ex) {
      // The viewer could be in e.g. a cross-origin <iframe> element,
      // fallback to dispatching the event at the current `document`.
      console.error("webviewerloaded:", ex);
      document.dispatchEvent(event);
    }
  }
  PDFViewerApplication.run(config);
}

// Regex Referenzen
const referenceTypes = {
  iso_iec: {
      regex: /(?:ISO(?:\/IEC)?|IEC)\s*(\d+(?:-\d+)*(?::\d{4})?)/g,
      linkBuilder: reference => `https://www.din.de/de/meta/suche/62730!search?query=${reference}`,
  },
  din: {
      regex: /DIN(?:[ ](?:EN|ISO|IEC|VDE))?[ ]\d+(?:-\d+)*(?::\d{4}(?:-\d{2})?)?/g,
      linkBuilder: reference => `https://www.din.de/de/meta/suche/62730!search?query=${reference}`
  },
  nist: {
      regex: /NIST(?: Special Publication| SP)?(?: IR)? [0-9]+(?:-[0-9]+)?(?:r[0-9]+)?/g,
      linkBuilder: reference => `https://www.nist.gov/search?s=${reference}`
  },
  rfc: {
      regex: /\(?RFC\)?\s*\d+/g,
      linkBuilder: reference => `https://www.rfc-editor.org/info/${reference.replace('+', '').replace(')', '').replace('(', '').replace('RFC', 'rfc')}` 
    },
  bsi_cs: {
      regex: /BSI-CS\s\d+/g,
      linkBuilder: reference => `https://www.bsi.bund.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/${reference.replace('+', '_')}.html`
  },
  ieee: {
      regex: /IEEE\s\d+\.?[1-9][0-9]*[A-Za-z]?[A-Za-z]?/g,
      linkBuilder: reference => `https://1.ieee802.org/security/${reference.replace('IEEE', '').replace('+', '').replace('.', '-')}/`
        },
  custom: {
      entries: {}, 
      linkBuilder: reference => referenceTypes.custom.entries[reference] || '#'
  }
};

function listReferences() {
  const pdfDocument = PDFViewerApplication.pdfDocument;
  const numPages = pdfDocument.numPages;
  let allReferences = {};

  // Manuell hinzugefügte Referenzen
  const customReferences = [
      { type: 'custom', reference: 'ISO/IEC 27007:2011', link: 'https://www.iso.org/standard/42506.html' },
      { type: 'custom', reference: 'ISO Standard 27001', link: 'https://www.iso.org/standard/27001' },
      { type: 'custom', reference: 'BSI-Standard 200-1', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-1-Managementsysteme-fuer-Informationssicherheit/bsi-standard-200-1-managementsysteme-fuer-informationssicherheit_node.html' },
      { type: 'custom', reference: 'BSI-Standard 200-2', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html' },
      { type: 'custom', reference: 'BSI-Standard 200-3', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-3-Risikomanagement/bsi-standard-200-3-risikomanagement_node.html' },
      { type: 'custom', reference: 'BSI-Standard 200-4', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-4-Business-Continuity-Management/bsi-standard-200-4_Business_Continuity_Management_node.html' },
      { type: 'custom', reference: 'BSI-Standard 100-4', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-100-4-Notfallmanagement/bsi-standard-100-4-notfallmanagement_node.html' },
      { type: 'custom', reference: 'BSI-Standards 200-1', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-1-Managementsysteme-fuer-Informationssicherheit/bsi-standard-200-1-managementsysteme-fuer-informationssicherheit_node.html' },
      { type: 'custom', reference: 'BSI-Standards 200-2', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html' },
      { type: 'custom', reference: 'BSI-Standards 200-3', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-3-Risikomanagement/bsi-standard-200-3-risikomanagement_node.html' },
      { type: 'custom', reference: 'BSI-Standards 200-4', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-4-Business-Continuity-Management/bsi-standard-200-4_Business_Continuity_Management_node.html' },
      { type: 'custom', reference: 'BSI-Standards 100-4', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-100-4-Notfallmanagement/bsi-standard-100-4-notfallmanagement_node.html' },
      { type: 'custom', reference: 'BSI-TR-02102', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr-02102.html' },
      { type: 'custom', reference: 'BSI TR-02102', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr-02102.html' },
      { type: 'custom', reference: 'BSI-TR-03138', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03138/ersetzendes-scannentr-resiscan.html' },
      { type: 'custom', reference: 'BSI TR-03138', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03138/ersetzendes-scannentr-resiscan.html' },
      { type: 'custom', reference: 'BSI-TR-03125', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03125/TR-03125_node.html' },
      { type: 'custom', reference: 'BSI TR-03125', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03125/TR-03125_node.html' },
      { type: 'custom', reference: 'BSI-TR-03108', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02/tr03108_node.html' },
      { type: 'custom', reference: 'BSI TR-03108', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02/tr03108_node.html' },
      { type: 'custom', reference: 'DSGVO', link: 'https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679' },
      { type: 'custom', reference: 'The Standard of Good Practice for Information Security', link: 'https://www.securityforum.org/solutions-and-insights/standard-of-good-practice-for-information-security/' },
      { type: 'custom', reference: 'IDW PS 980', link: 'https://www.idw.de/idw/idw-verlautbarungen/idw-ps-980.html' },
      { type: 'custom', reference: 'SDM', link: 'https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Technik/SDM.html' },
      { type: 'custom', reference: 'Leitfaden Backup / Recovery / Disaster Recovery', link: 'https://www.bitkom.org/sites/default/files/file/import/170125-LF-Backup-Recovery.pdf' },
      { type: 'custom', reference: 'Vorgehensmodelle für die betriebliche Anwendungsentwicklung', link: 'https://fg-wi-vm.gi.de/' },
      { type: 'custom', reference: 'Bedrohungsmodellierung (Threat Modeling) in der Softwareentwicklung', link: 'https://www.researchgate.net/publication/221307217_Bedrohungsmodellierung_Threat_Modeling_in_der_Softwareentwicklung' },
      { type: 'custom', reference: '„Entwicklung sicherer Webanwendungen“', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Studien/Webanwendungen/Webanw_Auftragnehmer.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'SÜG', link: 'https://www.gesetze-im-internet.de/s_g/BJNR086700994.html' },
      { type: 'custom', reference: 'Geheimschutzhandbuch der Wirtschaft (GHB)', link: 'https://www.bmwk-sicherheitsforum.de/handbuch/367,0,0,1,0.html?fk_menu=0' },
      { type: 'custom', reference: 'BSI-Schrift 7164', link: 'https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Zulassung/Hinweise-zur-Liste-der-zugelassenen-IT-Sicherheitsprodukte-und-systeme/hinweise-zur-liste-der-zugelassenen-it-sicherheitsprodukte-und-systeme.html' },
      { type: 'custom', reference: 'VS-Produktkatalog des BSI', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Zulassung/VS-Produktkatalog_BSI.pdf?__blob=publicationFile&v=18' },
      { type: 'custom', reference: 'Registraturrichtlinie für das Bearbeiten und Verwalten von Schriftgut in Bundesministerien', link: 'https://www.bmi.bund.de/SharedDocs/downloads/DE/veroeffentlichungen/themen/ministerium/registraturrichtlinie.html' },
      { type: 'custom', reference: 'Konkretisierung der Anforderungen an die gemäß § 8a Absatz 1 BSIG umzusetzenden Maßnahmen', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KRITIS/Konkretisierung_Anforderungen_Massnahmen_KRITIS.pdf?__blob=publicationFile&v=3' },
      { type: 'custom', reference: 'Mindeststandard des BSI zur Protokollierung und Detektion von Cyber-Angriffen', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_BSI_Protokollierung_und_Detektion_Version_2_0.pdf?__blob=publicationFile&v=3' },
      { type: 'custom', reference: 'The Art of Software Testing', link: 'https://malenezi.github.io/malenezi/SE401/Books/114-the-art-of-software-testing-3-edition.pdf' },
      { type: 'custom', reference: 'Grundregeln zur Absicherung von Fernwartungszugängen', link: 'https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_054.pdf?__blob=publicationFile&v=2' },
      { type: 'custom', reference: 'Anforderungskatalog Cloud Computing (C5)', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html' },
      { type: 'custom', reference: 'Security Guidance for Critical Areas of Focus in Cloud Computing', link: 'https://cloudsecurityalliance.org/artifacts/security-guidance-v4' },
      { type: 'custom', reference: 'Cloud Computing: Benefits, Risks and Recommendations for Information Security', link: 'https://www.enisa.europa.eu/sites/default/files/all_files/ENISA%20-%20Cloud%20Computing%20-%20final.pdf' },
      { type: 'custom', reference: 'Leitfaden Business Process Outsourcing: BPO als Chance für den Standort Deutschland“', link: 'https://www.bitkom.org/Bitkom/Publikationen/Leitfaden-Business-Process-Outsourcing.html' },
      { type: 'custom', reference: 'Leitfaden Rechtliche Aspekte von Outsourcing in der Praxis', link: 'https://www.bitkom.org/Bitkom/Publikationen/Rechtliche-Aspekte-von-Outsourcing-in-der-Praxis.html' },
      { type: 'custom', reference: 'Leitfaden zur Umsetzung rechtlicher Rahmenbedingungen', link: 'https://www.bitkom.org/sites/default/files/file/import/BITKOM-Leitfaden-Compliance-in-IT-Outsourcing-Projekten-290806.pdf' },
      { type: 'custom', reference: 'BSI-Leitfaden zur Einführung von Intrusion-Detection-Systemen', link: 'https://www.bsi.bund.de/DE/Service-Navi/Publikationen/Studien/IDS02/evids_ra_htm.html' },
      { type: 'custom', reference: 'Leitfaden IT-Forensik', link: 'https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Sicherheitspruefungen/IT-Forensik/forensik_node.html' },
      { type: 'custom', reference: 'Advanced Persistent Threats – Teil 4 Reaktion – Technische und organisatorische Maßnahmen für die Vorfallsbearbeitung', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Gefaehrdungen/APT/apt.html' },
      { type: 'custom', reference: 'BSI-PP-0040', link: 'https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/Archiv/PP_0040.html' },
      { type: 'custom', reference: 'CERT-EU Security Whitepaper 2014-007: Kerberos Golden Ticket Protection: Mitigating Pass-the-Ticket on Active Directory', link: 'https://cert.europa.eu/publications/security-guidance/CERT-EU_Security_Whitepaper_2014-007/pdf' },
      { type: 'custom', reference: 'Informationssicherheitsrevision: Ein Leitfaden für die IS-Revision auf Basis von IT-Grundschutz', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Leitfaden_IS-Revision-v4.pdf?__blob=publicationFile&v=2' },
      { type: 'custom', reference: 'Verbindliche Prüfthemen für die IS-Kurzrevision', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Pruefthemen_IS-Kurzrevision_v2_pdf.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'Revisionshandbuch zur Informationssicherheit nach UP Bund', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ISRevision/Muster_ISRevisionshandbuch-v1_pdf.pdf?__blob=publicationFile' },
      { type: 'custom', reference: 'Verschlusssachenanweisung (VSA)', link: 'https://www.bmi.bund.de/SharedDocs/downloads/DE/veroeffentlichungen/themen/sicherheit/verschlusssachenanweisung-vsa.pdf?__blob=publicationFile&v=5' },
      { type: 'custom', reference: '§ 8 Abs. 1 Satz 1 BSIG', link: 'https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/mindeststandards.html' },
      { type: 'custom', reference: 'Apps & Mobile Services – Tipps für Unternehmen', link: 'https://www.bitkom.org/sites/default/files/file/import/121214-Leitfaden-Apps-und-Mobile.pdf' },
      { type: 'custom', reference: 'Securing Mobile Apps – Embracing mobile, balancing control', link: 'https://www.securityforum.org/solutions-and-insights/securing-mobile-apps-embracing-mobile-balancing-control/' },
      { type: 'custom', reference: 'Migration auf TLS 1.2 – Handlungsleitfaden', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Archivdokumente/Migrationsleitfaden_Mindeststandard_BSI_TLS_Version_1_2.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'Sicheres Webhosting: Handlungsempfehlung für Webhoster', link: 'https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_068.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'Sicheres Bereitstellen von Webangeboten (ISi-Webserver)', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi_web_server_leitlinie.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'SAP ERP 6.0: Best Practice', link: 'https://www.dsag.de/wp-content/uploads/2021/12/150505_leitfaden_best-practice-sap-erp_rz.pdf' },
      { type: 'custom', reference: 'Oracle: Datenbank-Sicherheit – Grundüberlegungen', link: 'https://www.oracle.com/a/ocom/docs/wp-datenbank-sicherheit-grund-berlegungen-de.pdf' },
      { type: 'custom', reference: 'McAfee: Datenbanksicherheit in Virtualisierungs- und Cloud-Computing-Umgebungen', link: 'https://whitepaper.silicon.de/resource/datenbanksicherheit-in-virtualisierungs-und-cloud-computing-umgebungen/' },
      { type: 'custom', reference: 'Sicherheitsanforderung Datenbanksysteme', link: 'https://www.telekom.com/de/konzern/datenschutz-und-sicherheit/news/privacy-and-security-assessment-verfahren-342724' },
      { type: 'custom', reference: 'Best Practice Guide: Leitfaden Development ABAP 2.0', link: 'https://dsag.de/wp-content/uploads/2021/12/dsag_handlungsempfehlung_abap_2016_0.pdf' },
      { type: 'custom', reference: 'Guidelines on Electronic Mail Security', link: 'https://csrc.nist.gov/pubs/sp/800/45/ver2/final' },
      { type: 'custom', reference: 'Empfehlungen für den sicheren Einsatz von Application Delivery Controllern (ADC)', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Hilfsmittel/Hilfsmittel_Empfehlung_ApplicationDeliveryController_v1.pdf?__blob=publicationFile&v=1' },
      { type: 'custom', reference: 'SP 800-179 Rev. 1 (DRAFT): Guide to Securing Apple macOS 10.12 Systems for IT Professionals: A NIST Security Configuration Checklist', link: 'https://csrc.nist.gov/pubs/sp/800/179/r1/ipd' },
      { type: 'custom', reference: 'IEEE Standard Schutzprofil für Multifunktionsgeräte', link: 'https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/aktuell/PP_0058.html' },
      { type: 'custom', reference: 'IEEE 802.11', link: 'https://www.ieee802.org/11/' },
      { type: 'custom', reference: 'ICS-Security-Kompendium', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.pdf?__blob=publicationFile' },
      { type: 'custom', reference: 'Sicherheit von Geräten im Internet der Dinge', link: 'https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_128.pdf?__blob=publicationFile&v=3' },
      { type: 'custom', reference: 'Strategic Principles for securing the Internet of Things (IoT)', link: 'https://www.dhs.gov/sites/default/files/publications/Strategic_Principles_for_Securing_the_Internet_of_Things-2016-1115-FINAL_v2-dg11.pdf' },
      { type: 'custom', reference: 'ETSI EN 303 645', link: 'https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf' },
      { type: 'custom', reference: 'Empfehlungen für Fortbildungs- und Qualifizierungsmaßnahmen im ICS-Umfeld', link: 'https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_123.html' },
      { type: 'custom', reference: 'ICS Security Kompendium', link: 'https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security_kompendium_pdf.html' },
      { type: 'custom', reference: 'Whitepaper: Anforderungen an sichere Steuerungs- und Telekommunikationssysteme', link: 'https://www.bdew.de/service/anwendungshilfen/whitepaper-anforderungen-sichere-steuerungs-telekommunikationssysteme/' },
      { type: 'custom', reference: 'VDI/VDE 2180', link: 'https://www.vdi.de/richtlinien/details/vdivde-2180-blatt-1-funktionale-sicherheit-in-der-prozessindustrie-einfuehrung-begriffe-konzeption' },
      { type: 'custom', reference: 'VDI/VDE 2182', link: 'https://www.vdi.de/richtlinien/details/vdivde-2182-blatt-1-informationssicherheit-in-der-industriellen-automatisierung-allgemeines-vorgehensmodell' },
      { type: 'custom', reference: 'Fernwartung im industriellen Umfeld', link: 'https://www.allianz-fuer-cybersicherheit.de/SharedDocs/Downloads/Webs/ACS/DE/BSI-CS/BSI-CS_108.pdf?__blob=publicationFile' },
      { type: 'custom', reference: 'ISi-Reihe', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/ISI-Reihe/isi-reihe_node.html' },
      { type: 'custom', reference: 'ISi-LANA', link: 'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/ISI-Reihe/isi-reihe_node.html' },
      { type: 'custom', reference: 'BSI-TL02103', link: 'https://www.bsi.bund.de/DE/Service-Navi/Publikationen/TL-sichere-TK-Anlagen/TL02103_htm.html' },
      { type: 'custom', reference: 'Sicherungsleitfaden Perimeter', link: 'https://shop.vds.de/download/vds-3143' },
      { type: 'custom', reference: 'DGUV Vorschrift 4', link: 'https://publikationen.dguv.de/widgets/pdf/download/article/1457' },
      { type: 'custom', reference: 'DGUV Vorschrift 3', link: 'https://publikationen.dguv.de/widgets/pdf/download/article/1052' },
      { type: 'custom', reference: 'Richtlinie VdS 2311', link: 'https://vds.de/nachrichten/2021/newsdetailseite/richtlinien-vds-2311' },
      { type: 'custom', reference: 'Arbeitsstättenverordnung', link: 'https://www.baua.de/DE/Themen/Arbeitsgestaltung/Arbeitsstaetten/Arbeitsstaettenverordnung' },
      { type: 'custom', reference: 'IT-Sicherheit und Datenschutz im vernetzten Fahrzeug', link: 'https://publica.fraunhofer.de/entities/publication/ccac1d31-ae62-45e3-aead-bc7d4b075b10' },
      { type: 'custom', reference: 'Security Issues and Vulnerabilities in Connected Car Systems', link: 'https://ieeexplore.ieee.org/document/7223297' },
      { type: 'custom', reference: 'VDI 4700', link: 'https://www.vdi.de/richtlinien/details/vdi-4700-blatt-1-begriffe-der-bau-und-gebaeudetechnik' },
      { type: 'custom', reference: 'VDI 3814', link: 'https://www.vdi.de/richtlinien/unsere-richtlinien-highlights/vdi-3814' },
      { type: 'custom', reference: 'VDMA 24774', link: 'https://www.dinmedia.de/de/technische-regel/vdma-24774/364326838' },  
    ];

  for (let pageNum = 1; pageNum <= numPages; pageNum++) {
      pdfDocument.getPage(pageNum).then(page => {
          page.getTextContent().then(textContent => {
              let pageText = '';
              let lastItemY = null;

              textContent.items.forEach(item => {
                  if (lastItemY !== null && item.transform[5] !== lastItemY) {
                      pageText += ' ';
                  }
                  pageText += item.str;
                  lastItemY = item.transform[5];
              });

              // Prüfen, ob benutzerdefinierte Referenzen im Text vorkommen
              let foundCustomReferences = new Set();
              customReferences.forEach(({ type, reference, link }) => {
                  if (pageText.includes(reference)) {
                      foundCustomReferences.add(reference);
                      if (!allReferences[type]) {
                          allReferences[type] = {};
                      }
                      if (allReferences[type][reference]) {
                          allReferences[type][reference].pages.push(pageNum);
                      } else {
                          allReferences[type][reference] = { pages: [pageNum], link };
                      }
                  }
              });

              // Standard Referenzen nur hinzufügen, wenn sie nicht als Custom gefunden wurden
              for (const type in referenceTypes) {
                  if (referenceTypes[type].regex) {
                      const regex = referenceTypes[type].regex;
                      let matches;

                      while ((matches = regex.exec(pageText)) !== null) {
                          const reference = matches[0];
                          if (!foundCustomReferences.has(reference)) {
                              if (allReferences[type] && allReferences[type][reference]) {
                                  allReferences[type][reference].pages.push(pageNum);
                              } else {
                                  if (!allReferences[type]) {
                                      allReferences[type] = {};
                                  }
                                  allReferences[type][reference] = { pages: [pageNum] };
                              }
                          }
                      }
                  }
              }

              if (pageNum === numPages) {
                  displayReferences(allReferences);
              }
          });
      });
  }
}

// Referenzen in eigenem Fenster anzeigen
function displayReferences(allReferences) {
  let referencesList = '<h2>Referenzen:</h2>';
  for (const type in allReferences) {
      for (const reference in allReferences[type]) {
          const pages = allReferences[type][reference].pages.join(', ');
          const link = allReferences[type][reference].link || referenceTypes[type].linkBuilder(reference.replace(/\s/g, '+'));
          referencesList += `<li><a href="${link}" target="_blank">${reference} (Seite ${pages})</a></li>`;
      }
      referencesList += '</ul>';
  }

  let win = window.open("", "Referenzen", "width=800,height=600,scrollbars=yes");
  win.document.body.innerHTML = referencesList;
}

document.getElementById('References').addEventListener('click', listReferences);


document.getElementById('Inhaltsverzeichnis').addEventListener('click', () => {
  findAndJumpToFirstOccurrence('Inhaltsverzeichnis');
});

// Zum Inhaltsverzeichnis springen
async function findAndJumpToFirstOccurrence(searchText) {
  const pdfDocument = PDFViewerApplication.pdfDocument;
  const numPages = pdfDocument.numPages;

  for (let pageNum = 1; pageNum <= numPages; pageNum++) {
      const page = await pdfDocument.getPage(pageNum);
      const textContent = await page.getTextContent();
      let pageText = '';
      let lastItemY = null;

      textContent.items.forEach(item => {
          if (lastItemY !== null && item.transform[5] !== lastItemY) {
              pageText += ' ';
          }
          pageText += item.str;
          lastItemY = item.transform[5];
      });

      const lowerPageText = pageText.toLowerCase();
      const lowerSearchText = searchText.toLowerCase();

      const index = lowerPageText.indexOf(lowerSearchText);
      if (index !== -1) {
          PDFViewerApplication.pdfViewer.currentPageNumber = pageNum;
          return; // Beende die Suche nach dem ersten Fund
      }
  }
  alert('Inhaltsverzeichnis nicht gefunden.');
}

let regexSearchDiv = null; // Variable, um das Suchfeld zu speichern

// Suchfeld anzeigen
function toggleRegexSearch() {
    if (regexSearchDiv) {
        document.body.removeChild(regexSearchDiv);
        regexSearchDiv = null;
    } else {
        regexSearchDiv = document.createElement('div');
        regexSearchDiv.style.position = 'fixed';
        regexSearchDiv.style.top = '35px';
        regexSearchDiv.style.right = '250px';
        regexSearchDiv.style.backgroundColor = 'grey';
        regexSearchDiv.style.padding = '10px';
        regexSearchDiv.innerHTML = `
            <input type="text" id="regexInput" placeholder="Regex eingeben" style="width: 300px;"> 
            <button id="regexSearchButton">Suchen</button>
        `;
        document.body.appendChild(regexSearchDiv);

        const regexInput = document.getElementById('regexInput');
        regexInput.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                const regexString = regexInput.value;
                try {
                    const regex = new RegExp(regexString, 'g');
                    findAllRegexMatches(regex);
                } catch (e) {
                    alert('Ungültiger Regex-Ausdruck.');
                }
            }
        });

        // Suche auslösen
        document.getElementById('regexSearchButton').addEventListener('click', () => {
            const regexString = regexInput.value;
            try {
                const regex = new RegExp(regexString, 'g');
                findAllRegexMatches(regex);
            } catch (e) {
                alert('Ungültiger Regex-Ausdruck.');
            }
        });
    }
}

document.getElementById('Regex').addEventListener('click', toggleRegexSearch);

// Suchfeld mit STRG+X öffnen
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'x') {
        toggleRegexSearch();
    }
});

// Regexsuche durchführen
async function findAllRegexMatches(regex) {
    const pdfDocument = PDFViewerApplication.pdfDocument;
    const numPages = pdfDocument.numPages;
    let allMatches = {};

    for (let pageNum = 1; pageNum <= numPages; pageNum++) {
        const page = await pdfDocument.getPage(pageNum);
        const textContent = await page.getTextContent();
        let pageText = '';
        let lastItemY = null;

        textContent.items.forEach(item => {
            if (lastItemY !== null && item.transform[5] !== lastItemY) {
                pageText += ' ';
            }
            pageText += item.str;
            lastItemY = item.transform[5];
        });

        let match;
        while ((match = regex.exec(pageText)) !== null) {
            const sentence = findSentence(pageText, match.index, match[0].length);
            if (!allMatches[pageNum]) {
                allMatches[pageNum] = [];
            }
            allMatches[pageNum].push(sentence);
        }
    }

    if (Object.keys(allMatches).length > 0) {
        displayRegexMatches(allMatches);
    } else {
        alert('Keine Übereinstimmungen gefunden.');
    }
}

// Satz abgrenzen, in dem sich der Regex Match befindet
function findSentence(text, matchIndex, matchLength) {
  const separators = ['. ', ': ', '? ', '! ', '; ', '• ', '\n'];
  let start = 0;
  let end = text.length;

  for (const separator of separators) {
      const tempStart = text.lastIndexOf(separator, matchIndex);
      if (tempStart !== -1 && tempStart + separator.length > start) {
          start = tempStart + separator.length;
      }

      const tempEnd = text.indexOf(separator, matchIndex + matchLength);
      if (tempEnd !== -1 && tempEnd < end) {
          end = tempEnd;
      }
  }

  return text.substring(start, end).trim();
}

// Matches anzeigen
function displayRegexMatches(matches) {
  let matchesList = '<h2>Regex Übereinstimmungen:</h2><ul>';
  for (const pageNum in matches) {
      let pageMatches = matches[pageNum];
      let displaySentences = [];

      for (let i = 0; i < pageMatches.length; i++) {
          let sentence = pageMatches[i];
          displaySentences.push(sentence.replace(new RegExp(document.getElementById('regexInput').value, 'g'), match => `<b>${match}</b>`));
          if (i < pageMatches.length - 1) { // Trennung einfügen, außer beim letzten Satz
              displaySentences.push('[...]');
          }
      }

      matchesList += `<li>Seite ${pageNum}: ${displaySentences.join(' ')}</li>`;
  }
  matchesList += '</ul>';

  let win = window.open("", "Regex Matches", "width=800,height=600,scrollbars=yes");
  win.document.body.innerHTML = matchesList;
}

// Block the "load" event until all pages are loaded, to ensure that printing
// works in Firefox; see https://bugzilla.mozilla.org/show_bug.cgi?id=1618553
document.blockUnblockOnload?.(true);

if (
  document.readyState === "interactive" ||
  document.readyState === "complete"
) {
  webViewerLoad();
} else {
  document.addEventListener("DOMContentLoaded", webViewerLoad, true);
}

export {
  PDFViewerApplication,
  AppConstants as PDFViewerApplicationConstants,
  AppOptions as PDFViewerApplicationOptions,
};
