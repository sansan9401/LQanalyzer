#include <iostream>
#include <TChain.h>
#include <TClonesArray.h>
#include <TString.h>
#include <map>

#include <TSystem.h>
#include <TROOT.h>
#include <TMath.h>
#include <TLorentzVector.h>
#include <TRandom3.h>


class rochcor2012 {
 public:
  rochcor2012();
  rochcor2012(int seed);
  ~rochcor2012();
  
  void momcor_mc(TLorentzVector&, float, int, float&);
  void momcor_data(TLorentzVector&, float, int, float&);
  
  float zptcor(float);
  int etabin(float);
  int phibin(float);
  
 private:
  
  TRandom3 eran;
  TRandom3 sran;
  
  
  //  static float netabin[9] = {-2.4,-2.1,-1.4,-0.7,0.0,0.7,1.4,2.1,2.4};
  static const double pi;
  static const float netabin[9];
  
  static const float genm_smr; //gen mass peak with eta dependent gaussian smearing => better match in Z mass profile vs. eta/phi
  static const float genm; //gen mass peak without smearing => Z mass profile vs. eta/phi in CMS note
  
  static const float mrecm; //rec mass peak in MC (2011A)
  static const float drecm; //rec mass peak in data (2011A)
  static const float mgscl_stat; //stat. error of global factor for mass peak in MC (2011A)  
  static const float mgscl_syst; //syst. error of global factor for mass peak in MC (2011A)  
  static const float dgscl_stat; //stat. error of global factor for mass peak in data (2011A)
  static const float dgscl_syst; //syst. error of global factor for mass peak in data (2011A)
      
  static const float sf[8];
  static const float sfer[8];
  
  static const float gsf[8];
  static const float gsfer[8];
  
  //---------------------------------------------------------------------------------------------
  
  static const float dcor_bf[8][8];  
  static const float dcor_ma[8][8];
  static const float mcor_bf[8][8];
  static const float mcor_ma[8][8];
  static const float dcor_bfer[8][8];  
  static const float dcor_maer[8][8];
  static const float mcor_bfer[8][8];
  static const float mcor_maer[8][8];
  
  //=======================================================================================================
  
  static const float dmavg[8][8];  
  static const float dpavg[8][8];  
  static const float mmavg[8][8];  
  static const float mpavg[8][8];
  
  //===============================================================================================
  //parameters for Z pt correction
  static const int nptbins=84;
  static const float ptlow[85];    
  
  static const float zptscl[84];
  static const float zptscler[84];

  float mptsys_mc_dm[8][8];
  float mptsys_mc_da[8][8];
  float mptsys_da_dm[8][8];
  float mptsys_da_da[8][8];

  float gscler_mc_dev;
  float gscler_da_dev;
};
  
