#ifndef ROCHCOR2015_H
#define ROCHCOR2015_H

#include <iostream>
#include <map>
#include "TChain.h"
#include "TClonesArray.h"
#include "TString.h"

#include "TSystem.h"
#include "TROOT.h"
#include "TMath.h"
#include "TLorentzVector.h"
#include "TRandom3.h"

#include "RoccoR.h"

class rochcor2015 {
 public:
  rochcor2015();
  rochcor2015(int seed);
  ~rochcor2015();
  
  void momcor_mc(TLorentzVector&, float, int, float&);
  void momcor_data(TLorentzVector&, float, int, float&);
  
  int aetabin(double);
  int etabin(double);
  int phibin(double);
  
 private:
  
  TRandom3 eran;
  TRandom3 sran;
    
  static const double pi;
  static const double netabin[25];
  static const double anetabin[13];
  
  static const double mu_mass;
  static const double genm_smr; //gen mass peak with eta dependent gaussian smearing => better match in Z mass profile vs. eta/phi
  static const double genm; //gen mass peak without smearing => Z mass profile vs. eta/phi in CMS note
  
  static const double mgscl; //rec mass peak scale for MC
  static const double dgscl; //rec mass peak scale for data
  static const double mgscl_stat; //stat. error of global factor for mass peak in MC 
  static const double mgscl_syst; //syst. error of global factor for mass peak in MC  
  static const double dgscl_stat; //stat. error of global factor for mass peak in data 
  static const double dgscl_syst; //syst. error of global factor for mass peak in data 
  static const double dgscl_iter; //one more iteration to fix offset
  static const double mgscl_iter; //one more iteration to fix offset

  //-----------------------------------------------

  static const double dcor_bf[2][16][24];  
  static const double dcor_ma[2][16][24];
  static const double mcor_bf[16][24];
  static const double mcor_ma[16][24];
  static const double dcor_bfer[2][16][24];  
  static const double dcor_maer[2][16][24];
  static const double mcor_bfer[16][24];
  static const double mcor_maer[16][24];
  
  //===============================================
  
  static const double dmavg[2][16][24];  
  static const double dpavg[2][16][24];  
  static const double mmavg[16][24];  
  static const double mpavg[16][24];
  static const double dmavger[2][16][24];  
  static const double dpavger[2][16][24];  
  static const double mmavger[16][24];  
  static const double mpavger[16][24];

  static const double dd[12];
  static const double dder[12];
  static const double md[12];
  static const double mder[12];  

  static const double dscl[24];
  static const double mscl[24];
  //===============================================

  double mptsys_mc_dm[16][24];
  double mptsys_mc_da[16][24];
  double mptsys_da_dm[16][24];
  double mptsys_da_da[16][24];

  double gscler_mc_dev;
  double gscler_da_dev;


};
#endif
