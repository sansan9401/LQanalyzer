#include <string.h>
#include "TChain.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TTree.h"
#include "TKey.h"
#include <iostream>
#include <TStyle.h>
#include "TCanvas.h"
#include "TLegend.h"

#include "TString.h"

#include <sstream>      // std::stringstream

void setTDRStyle();
bool CheckFile(TFile* f);
bool CheckHist(TH2* h);


void MakeFRRootFile(){
  
  TString path= "/data2/CAT_SKTreeOutput/JobOutPut/jalmond/LQanalyzer//data/output/CAT/FakeRateCalculator_El/periodBtoH/";

  TFile * fdata = new TFile(path + "FakeRateCalculator_El_data_DoubleEG_cat_v8-0-7.root");
  TFile * fmc = new TFile(path + "FakeRateCalculator_El_mc_v8-0-7.root");
  cout << path + "FakeRateCalculator_El_data_DoubleEG_cat_v8-0-7.root" << endl;
  if(!fdata)cout << "No Data" << endl;
  if (!fmc) cout << "No MC" << endl;
  /// Set Plotting style
  setTDRStyle();
  gStyle->SetPalette(1);
    
  TString outfile = "FakeRate13TeV_2016_opt.root";
  TFile* fout = new TFile(outfile.Data(),"RECREATE");
  fout->cd();

  std::vector<TString> fakes40;
  fakes40.push_back("40_pt_eta");
  //fakes40.push_back("60_pt_eta");
  //fakes40.push_back("40_pt_eta");
  //fakes40.push_back("30_pt_eta");
  //
  std::vector<TString> isocut;


  int nmva=98;
  int ndxy=5;
  int ndz=3;
  int niso=5;
  vector<TString> vcut_mva_s;

  for(unsigned int imva=0; imva < nmva; imva++){
    float cut_dmva = float(imva)*0.01 -0.01;
    stringstream ss;
    ss << cut_dmva;
    vcut_mva_s.push_back(TString(ss.str()));
  }
  vector<TString> vcut_dxy_b_s;

  for(unsigned int dxy_b=0;dxy_b < ndxy; dxy_b++){
    float cut_dxy_b =  float(dxy_b)*0.01 + 0.01;
    stringstream ss;
    ss <<cut_dxy_b;
    vcut_dxy_b_s.push_back(TString(ss.str()));
  }
  vector<TString> vcut_dz_b_s;

  for(unsigned int dz_b=0;dz_b < ndz; dz_b++){
    float cut_dz_b =  float(dz_b)*0.02 + 0.04;
    stringstream ss;
    ss <<cut_dz_b;
    vcut_dz_b_s.push_back(TString(ss.str()));
  }


  vector<TString> vcut_iso_b_s;
  for(unsigned int iso_b=0;iso_b < niso; iso_b++){
    float cut_iso_b = float(iso_b)*0.01 + 0.05;
    stringstream ss;
    ss <<cut_iso_b;
    vcut_iso_b_s.push_back(TString(ss.str()));
  }

  //// Loop over cuts and fill loose and tight el and get fake rates for ID                                                                                                   
  for(unsigned int imva=0; imva < vcut_mva_s.size(); imva++){
    for(unsigned int dxy_b=0; dxy_b < vcut_dxy_b_s.size(); dxy_b++){
      for(unsigned int dz_b=0; dz_b < vcut_dz_b_s.size(); dz_b++){
	for(unsigned int iso_b=0; iso_b < vcut_iso_b_s.size(); iso_b++){
	  
	  isocut.push_back("dijet_mva"+vcut_mva_s[imva]+"_iso"+vcut_iso_b_s[iso_b]+"_dxy"+vcut_dxy_b_s[dxy_b]+"_dz"+vcut_dz_b_s[dz_b]);
	}
      }
    }
  }


  for(vector<TString>::iterator it2 = fakes40.begin(); it2!=fakes40.end(); ++it2){
    for(vector<TString>::iterator it3 = isocut.begin(); it3!=isocut.end(); ++it3){
      
      if(!CheckFile(fdata))return;
      if(!CheckFile(fmc))return;
      TString denom ="LooseEl"  + *it3 +"_"+ *it2;
      TString num ="TightEl"  +  *it3 + "_"+*it2;
      
      
      TH2D* h_pt_num= (TH2D*)fdata->Get(num.Data());
      TH2D* h_pt_denom= (TH2D*)fdata->Get(denom.Data());
      
      cout << h_pt_num << " " << h_pt_denom << endl;
      cout << num << " " << denom << endl;
      CheckHist(h_pt_denom);
      CheckHist(h_pt_num);
      TH2D* h_mcpt_num= (TH2D*)fmc->Get(num.Data());
      TH2D* h_mcpt_denom= (TH2D*)fmc->Get(denom.Data());
      CheckHist(h_mcpt_denom);
      CheckHist(h_mcpt_num);
      
      TString name =*it2 + *it3;
      
      TH2D* eff_rate = (TH2D*)h_pt_num->Clone(("FakeRate_" + name).Data());
      TH2D* hratedenom = (TH2D*)h_pt_denom->Clone((name +"_denom").Data());
      eff_rate->Add(h_mcpt_num,-1.);
      hratedenom->Add(h_mcpt_denom, -1.);
      eff_rate->Divide(eff_rate,hratedenom,1.,1.,"cl=0.683 b(1,1) mode");
      eff_rate->Write();
    }
    
  }
  
  
  return;

}

  
bool CheckFile(TFile* f ){
    bool file_exist = true;
    if(!f){
      cout << "File " << f->GetName() << " does not exist. Exiting " << endl;
      file_exist = false;
    }
    
    return file_exist;
}

bool CheckHist(TH2* h ){
  bool hist_exist = true;
  if(!h){
    cout << "No histogram with name " << h->GetName() << endl;
    hist_exist= false;
  }
  return hist_exist;
}






  void setTDRStyle() {
    TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

    // For the canvas:
    tdrStyle->SetCanvasBorderMode(0);
    tdrStyle->SetCanvasColor(kWhite);
    tdrStyle->SetCanvasDefH(600); //Height of canvas
    tdrStyle->SetCanvasDefW(600); //Width of canvas
    tdrStyle->SetCanvasDefX(0);   //POsition on screen
    tdrStyle->SetCanvasDefY(0);

    // For the Pad:
    tdrStyle->SetPadBorderMode(0);
    // tdrStyle->SetPadBorderSize(Width_t size = 1);
    tdrStyle->SetPadColor(kWhite);
    tdrStyle->SetPadGridX(false);
    tdrStyle->SetPadGridY(false);
    tdrStyle->SetGridColor(0);
    tdrStyle->SetGridStyle(3);
    tdrStyle->SetGridWidth(1);


    // For the frame:
    tdrStyle->SetFrameBorderMode(0);
    tdrStyle->SetFrameBorderSize(1);
    tdrStyle->SetFrameFillColor(0);
    tdrStyle->SetFrameFillStyle(0);
    tdrStyle->SetFrameLineColor(1);
    tdrStyle->SetFrameLineStyle(1);
    tdrStyle->SetFrameLineWidth(1);


    // For the histo:
    // tdrStyle->SetHistFillColor(1);
    // tdrStyle->SetHistFillStyle(0);
    tdrStyle->SetHistLineColor(1);
    tdrStyle->SetHistLineStyle(0);
    tdrStyle->SetHistLineWidth(1);
    // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
    // tdrStyle->SetNumberContours(Int_t number = 20);
    tdrStyle->SetEndErrorSize(2);
    //  tdrStyle->SetErrorMarker(20);
    //  tdrStyle->SetErrorX(0.);

    tdrStyle->SetMarkerStyle(20);

    //For the fit/function:
    tdrStyle->SetOptFit(1);
    tdrStyle->SetFitFormat("5.4g");
    tdrStyle->SetFuncColor(2);
    tdrStyle->SetFuncStyle(1);
    tdrStyle->SetFuncWidth(1);

    //For the date:
    tdrStyle->SetOptDate(0);
    // tdrStyle->SetDateX(Float_t x = 0.01);

    // tdrStyle->SetDateY(Float_t y = 0.01);

    // For the statistics box:
    tdrStyle->SetOptFile(0);
    tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
    tdrStyle->SetStatColor(kWhite);
    tdrStyle->SetStatFont(42);
    tdrStyle->SetStatFontSize(0.025);
    tdrStyle->SetStatTextColor(1);
    tdrStyle->SetStatFormat("6.4g");
    tdrStyle->SetStatBorderSize(1);
    tdrStyle->SetStatH(0.1);
    tdrStyle->SetStatW(0.15);
    // tdrStyle->SetStatStyle(Style_t style = 1001);
    // tdrStyle->SetStatX(Float_t x = 0);
    // tdrStyle->SetStatY(Float_t y = 0);

    // Margins:
    tdrStyle->SetPadTopMargin(0.05);
    tdrStyle->SetPadBottomMargin(0.12);
    tdrStyle->SetPadLeftMargin(0.12);
    tdrStyle->SetPadRightMargin(0.1);

    // For the Global title:

    tdrStyle->SetOptTitle(0);
    tdrStyle->SetTitleFont(42);
    tdrStyle->SetTitleColor(1);
    tdrStyle->SetTitleTextColor(1);
    tdrStyle->SetTitleFillColor(10);
    tdrStyle->SetTitleFontSize(0.05);
    // tdrStyle->SetTitleH(0); // Set the height of the title box
    // tdrStyle->SetTitleW(0); // Set the width of the title box
    // tdrStyle->SetTitleX(0); // Set the position of the title box
    // tdrStyle->SetTitleY(0.985); // Set the position of the title box
    // tdrStyle->SetTitleStyle(Style_t style = 1001);
    // tdrStyle->SetTitleBorderSize(2);

    // For the axis titles:

    tdrStyle->SetTitleColor(1, "XYZ");
    tdrStyle->SetTitleFont(42, "XYZ");
    tdrStyle->SetTitleSize(0.06, "XYZ");
    // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
    // tdrStyle->SetTitleYSize(Float_t size = 0.02);
    tdrStyle->SetTitleXOffset(0.9);
    tdrStyle->SetTitleYOffset(1.4);
    // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset


    // For the axis labels:

    tdrStyle->SetLabelColor(1, "XYZ");
    tdrStyle->SetLabelFont(42, "XYZ");
    tdrStyle->SetTitleSize(0.06, "XYZ");
    // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
    // tdrStyle->SetTitleYSize(Float_t size = 0.02);
    tdrStyle->SetTitleXOffset(0.9);
    tdrStyle->SetTitleYOffset(1.4);
    // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

    // For the axis labels:

    tdrStyle->SetLabelColor(1, "XYZ");
    tdrStyle->SetLabelFont(42, "XYZ");
    tdrStyle->SetLabelOffset(0.007, "XYZ");
    tdrStyle->SetLabelSize(0.05, "XYZ");

    // For the axis:

    tdrStyle->SetAxisColor(1, "XYZ");
    tdrStyle->SetStripDecimals(kTRUE);
    tdrStyle->SetTickLength(0.03, "XYZ");
    tdrStyle->SetNdivisions(510, "XYZ");
    tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
    tdrStyle->SetPadTickY(1);

    // Change for log plots:
    tdrStyle->SetOptLogx(0);
    tdrStyle->SetOptLogy(0);
    tdrStyle->SetOptLogz(0);

    // Postscript options:
    tdrStyle->SetPaperSize(20.,20.);


    // tdrStyle->SetLineScalePS(Float_t scale = 3);
    // tdrStyle->SetLineStyleString(Int_t i, const char* text);
    // tdrStyle->SetHeaderPS(const char* header);
    // tdrStyle->SetTitlePS(const char* pstitle);

    // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
    // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
    // tdrStyle->SetPaintTextFormat(const char* format = "g");
    // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
    // tdrStyle->SetTimeOffset(Double_t toffset);
    // tdrStyle->SetHistMinimumZero(kTRUE);

    tdrStyle->cd();

  }
