#ifndef TriLeptonPlots_h
#define TriLeptonPlots_h

/// Standard includes
#include <string>
#include <iostream>

/// Root includes
#include "TH1D.h"
#include "TH2D.h"
#include "TH3D.h"

/// local includes
#include "StdPlots.h"
#include "KMuon.h"
#include "KJet.h"
#include "KElectron.h"
#include "KEvent.h"

using namespace snu;

class TriLeptonPlots : public StdPlots{
 
  Double_t dijetmass_tmp, dijetmass;

 
 public:
  
  // Default constructor
  TriLeptonPlots();
  
  // Main constructor
  TriLeptonPlots(TString name);
  
  // Destructor
  ~TriLeptonPlots();

  /// Get Map
  inline std::map<TString, TH1*> GetMap() const{return map_sig;}
  inline std::map<TString, TH2*> GetMap2() const{return map_sig2;}
  inline std::map<TString, TH3*> GetMap3() const{return map_sig3;}

  /// copy constructor
  TriLeptonPlots(const TriLeptonPlots& sp);  ///Copy constructor
  /// assigment operator
  TriLeptonPlots& operator=(const TriLeptonPlots& obj);
  float GetElectronISOEA(float eta);

  /// fill functions
  void Fill(snu::KEvent ev, std::vector<snu::KMuon>& muons, std::vector<snu::KJet>& jets, Double_t weight);
  void Fill(snu::KEvent ev, std::vector<snu::KElectron>& electrons, std::vector<snu::KJet>& jets, Double_t weight);
  void Fill(snu::KEvent ev, std::vector<snu::KMuon>& muons,std::vector<snu::KElectron>& electrons, std::vector<snu::KJet>& jets, Double_t weight);


  void Fill(TString name, double value, double weight);
  void Fill(TString name, double value, double value2, double weight);
  void Fill(TString name, double value, double value2, double value3, double weight);

  /// function to write out hists
  void Write();

 private:
  std::map<TString, TH1*> map_sig; 
  std::map<TString, TH2*> map_sig2; 
  std::map<TString, TH3*> map_sig3; 


};


#endif
