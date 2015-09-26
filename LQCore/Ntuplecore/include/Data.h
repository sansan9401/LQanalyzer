//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Aug 24 11:24:50 2012 by ROOT version 5.32/00
// from TTree tree/
// found on file: /mnt/hadoop/cms/store/user/fgior8/Summer12LJ/SingleMuB/RootTupleMakerV2_output_DATA_506_1_Y4H.root
//////////////////////////////////////////////////////////

#ifndef DATA_h
#define DATA_h

// STL include(s):
#include <string>
#include <vector>
#include <list>

#include <TROOT.h>


#include "LQCycleBaseNTuple.h"

// Forward declaration(s):
class TTree;
class TBranch;

namespace snu{
  class KMuon;
  class KElectron;
  class KEvent;
  class KJet;
  class KGenJet;
  class KTrigger;
  class KTruth;
}



class Data : public LQCycleBaseNTuple {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   //static Int_t kMaxtriggers = 48;


   Long64_t GetNEntries();
   UInt_t GetEventNumber();
   TTree          *output_tree;

   Data();
   ~Data();

   void      GetEvent(Long64_t entry)throw( LQError );
   Int_t    GetEntry(Long64_t entry);
   Int_t    Cut(Long64_t entry);
   Long64_t LoadTree(Long64_t entry);
   void Init(TTree *tree);
   Bool_t   Notify(); //remove if possible
   void     Show(Long64_t entry = -1); //remove if possible
   TTree* GetInputTree();
   void setBranchStatus(void);
   void CheckCaching();

   /// Connect an input variable                                                
   template< typename T >
     bool ConnectVariable(  const char* branchName,
			    T& variable, TBranch* br);
   /// Specialisation for object pointers                                                                                                                                      
   template< typename T >
     bool ConnectVariable(const char* branchName,
			  T*& variable, TBranch* br);   

   void Reset();
   void ConnectVariables(Bool_t setall);

   void ConnectEvent();
   void ConnectMuons();
   void ConnectElectrons();
   void ConnectPFJets();

   void ConnectTruth();
   void ConnectTrigger();
   void ConnectAllBranches();
   void ConnectMET();
   void SetLQNtupleInputType(bool lq);
     

   bool LQinput;
   Long64_t nentries;

   // Declaration of leaf types

   /// If needed (using SKTree input)
   std::vector<snu::KMuon>     *k_inputmuons;
   std::vector<snu::KElectron>     *k_inputelectrons;
   std::vector<snu::KJet>     *k_inputjets;
   std::vector<snu::KGenJet>     *k_inputgenjets;
   snu::KEvent     *k_inputevent;
   snu::KTrigger     *k_inputtrigger;
   std::vector<snu::KTruth>     *k_inputtruth;


   Bool_t          isData;
   std::vector<TBranch*> m_inputbranches;


   // Declaration of leaf types
   Int_t           run;
   Int_t           lumi;
   Int_t           event;
   std::vector<float>   *gen_pt;
   std::vector<std::string>  *vtrignames;
   std::vector<int>     *vtrigps;
   std::vector<float>   *gen_eta;
   std::vector<float>   *gen_phi;
   std::vector<float>   *gen_energy;
   std::vector<int>     *gen_status;
   std::vector<int>     *gen_pdgid;
   std::vector<int>     *gen_motherindex;
   Bool_t          HNHENoiseFilter;
   Bool_t          csctighthaloFilter;
   Bool_t          ecalDCTRFilter;
   Bool_t          eeBadScFilter;
   Bool_t          goodVertices;
   Int_t           GenTTCat;
   Int_t           genWeight_id1;
   Int_t           genWeight_id2;
   Int_t           hlt_2el33;
   Int_t           hlt_el12;
   Int_t           hlt_el16_el12_8;
   Int_t           hlt_el17;
   Int_t           hlt_el17_el12;
   Int_t           hlt_el23_el12;
   Int_t           hlt_el23_el12dz;
   Int_t           hlt_ele27eta2p1;
   Int_t           hlt_mu17_el12;
   Int_t           hlt_mu17_mu8;
   Int_t           hlt_mu17_tkmu8;
   Int_t           hlt_mu8_el17;
   Int_t           nGoodPV;
   Int_t           nPV;
   Int_t           nTrueInteraction;
   Float_t         genWeight;
   Float_t         genWeightQ;
   Float_t         genWeightX1;
   Float_t         genWeightX2;
   Float_t         lheWeight;
   Float_t         puWeight;
   Float_t         puWeightDn;
   Float_t         puWeightUp;
   std::vector<float>   *pdfWeight;
   Int_t           triggers_;
   std::string         triggers_first[100];
   Int_t           triggers_second[100];   //[triggers_]      
   std::vector<double>  *electrons_absIso03;
   std::vector<double>  *electrons_absIso04;
   std::vector<double>  *electrons_chIso03;
   std::vector<double>  *electrons_chIso04;
   std::vector<double>  *electrons_dxy;
   std::vector<double>  *electrons_dz;
   std::vector<double>  *electrons_energy;
   std::vector<double>  *electrons_eta;
   std::vector<double>  *electrons_isGsfCtfScPixChargeConsistent;
   std::vector<double>  *electrons_m;
   std::vector<double>  *electrons_nhIso03;
   std::vector<double>  *electrons_nhIso04;
   std::vector<double>  *electrons_phIso03;
   std::vector<double>  *electrons_phIso04;
   std::vector<double>  *electrons_phi;
   std::vector<double>  *electrons_pt;
   std::vector<double>  *electrons_puChIso03;
   std::vector<double>  *electrons_puChIso04;
   std::vector<double>  *electrons_q;
   std::vector<double>  *electrons_relIso03;
   std::vector<double>  *electrons_relIso04;
   std::vector<double>  *electrons_scEta;
   std::vector<double>  *electrons_shiftedEnDown;
   std::vector<double>  *electrons_shiftedEnUp;
   std::vector<double>  *electrons_x;
   std::vector<double>  *electrons_y;
   std::vector<double>  *electrons_z;
   std::vector<double>  *jets_CVSInclV2;
   std::vector<double>  *jets_energy;
   std::vector<double>  *jets_eta;
   std::vector<double>  *jets_isPFId;
   std::vector<double>  *jets_m;
   std::vector<double>  *jets_phi;
   std::vector<double>  *jets_pt;
   std::vector<double>  *jets_shiftedEnDown;
   std::vector<double>  *jets_shiftedEnUp;
   std::vector<double>  *jets_smearedRes;
   std::vector<double>  *jets_smearedResDown;
   std::vector<double>  *jets_smearedResUp;
   std::vector<double>  *jets_vtx3DSig;
   std::vector<double>  *jets_vtx3DVal;
   std::vector<double>  *jets_vtxMass;
   std::vector<double>  *jetsPuppi_CVSInclV2;
   std::vector<double>  *jetsPuppi_eta;
   std::vector<double>  *jetsPuppi_hadronFlavour;
   std::vector<double>  *jetsPuppi_m;
   std::vector<double>  *jetsPuppi_partonFlavour;
   std::vector<double>  *jetsPuppi_phi;
   std::vector<double>  *jetsPuppi_pt;
   std::vector<double>  *jetsPuppi_vtx3DSig;
   std::vector<double>  *jetsPuppi_vtx3DVal;
   std::vector<double>  *jetsPuppi_vtxMass;
   std::vector<double>  *met_phi;
   std::vector<double>  *met_pt;
   std::vector<double>  *met_sumet;
   std::vector<double>  *metNoHF_phi;
   std::vector<double>  *metNoHF_pt;
   std::vector<double>  *metNoHF_sumet;
   std::vector<double>  *metPfMva_phi;
   std::vector<double>  *metPfMva_pt;
   std::vector<double>  *metPfMva_sumet;
   std::vector<double>  *metPuppi_phi;
   std::vector<double>  *metPuppi_pt;
   std::vector<double>  *metPuppi_sumet;
   std::vector<double>  *muon_dxy;
   std::vector<double>  *muon_dz;
   std::vector<double>  *muon_energy;
   std::vector<double>  *muon_eta;
   std::vector<double>  *muon_m;
   std::vector<double>  *muon_normchi;
   std::vector<double>  *muon_phi;
   std::vector<double>  *muon_pt;
   std::vector<double>  *muon_q;
   std::vector<double>  *muon_relIso03;
   std::vector<double>  *muon_relIso04;
   std::vector<double>  *muon_shiftedEdown;
   std::vector<double>  *muon_shiftedEup;
   std::vector<double>  *muon_x;
   std::vector<double>  *muon_y;
   std::vector<double>  *muon_z;
   std::vector<double>  *slimmedGenJets_energy;
   std::vector<double>  *slimmedGenJets_eta;
   std::vector<double>  *slimmedGenJets_m;
   std::vector<double>  *slimmedGenJets_phi;
   std::vector<double>  *slimmedGenJets_pt;
   std::vector<double>  *vertices_ndof;
   std::vector<double>  *vertices_x;
   std::vector<double>  *vertices_y;
   std::vector<double>  *vertices_z;
   std::vector<bool>    *electrons_electronID_loose;
   std::vector<bool>    *electrons_electronID_medium;
   std::vector<bool>    *electrons_electronID_tight;
   std::vector<bool>    *electrons_electronID_veto;
   std::vector<bool>    *electrons_isPF;
   std::vector<bool>    *electrons_mcMatched;
   std::vector<bool>    *electrons_passConversionVeto;
   std::vector<bool>    *jets_isLoose;
   std::vector<bool>    *jets_isTight;
   std::vector<bool>    *jets_isTightLepVetoJetID;
   std::vector<bool>    *muon_isGlobal;
   std::vector<bool>    *muon_isLoose;
   std::vector<bool>    *muon_isMedium;
   std::vector<bool>    *muon_isPF;
   std::vector<bool>    *muon_isSoft;
   std::vector<bool>    *muon_isTight;
   std::vector<bool>    *muon_isTracker;
   std::vector<bool>    *muon_matched;
   std::vector<int>     *electrons_electronID_snu;
   std::vector<int>     *jets_hadronFlavour;
   std::vector<int>     *jets_partonFlavour;
   std::vector<int>     *jets_partonPdgId;
   std::vector<int>     *jets_vtxNtracks;
   std::vector<int>     *muon_matchedstations;
   std::vector<int>     *muon_trackerlayers;
   std::vector<int>     *muon_validhits;
   std::vector<int>     *muon_validmuonhits;
   std::vector<int>     *muon_validpixhits;

   // List of branches                                                                                                                                                                                                                                                       
   TBranch        *b_vtrignames;   //!                                                                                                                        
   TBranch        *b_vtrigps;   //!   

   TBranch        *b_run;   //!                                                                                                                                                                                                                                              
   TBranch        *b_lumi;   //!                                                                                                                                                                                                                                             
   TBranch        *b_event;   //!                                                                                                                                                                                                                                            
   TBranch        *b_gen_pt;   //!                                                                                                                                                                                                                                           
   TBranch        *b_gen_eta;   //!                                                                                                                                                                                                                                          
   TBranch        *b_gen_phi;   //!                                                                                                                                                                                                                                          
   TBranch        *b_gen_energy;   //!                                                                                                                                                                                                                                       
   TBranch        *b_gen_status;   //!                                                                                                                                                                                                                                       
   TBranch        *b_gen_pdgid;   //!                                                                                                                                                                                                                                        
   TBranch        *b_gen_motherindex;   //!                                                                                                                                                                                                                                  
   TBranch        *b_HNHENoiseFilter;   //!                                                                                                                                                                                                                                  
   TBranch        *b_csctighthaloFilter;   //!                                                                                                                                                                                                                               
   TBranch        *b_ecalDCTRFilter;   //!                                                                                                                                                                                                                                   
   TBranch        *b_eeBadScFilter;   //!                                                                                                                                                                                                                                    
   TBranch        *b_goodVertices;   //!                                                                                                                                                                                                                                     
   TBranch        *b_GenTTCat;   //!                                                                                                                                                                                                                                         
   TBranch        *b_genWeight_id1;   //!                                                                                                                                                                                                                                    
   TBranch        *b_genWeight_id2;   //!                                                                                                                                                                                                                                    
   TBranch        *b_hlt_2el33;   //!                                                                                                                                                                                                                                        
   TBranch        *b_hlt_el12;   //!                                                                                                                                                                                                                                         
   TBranch        *b_hlt_el16_el12_8;   //!                                                                                                                                                                                                                                  
   TBranch        *b_hlt_el17;   //!                                                                                                                                                                                                                                         
   TBranch        *b_hlt_el17_el12;   //!                                                                                                                                                                                                                                    
   TBranch        *b_hlt_el23_el12;   //!                                                                                                                                                                                                                                    
   TBranch        *b_hlt_el23_el12dz;   //!                                                                                                                                                                                                                                  
   TBranch        *b_hlt_ele27eta2p1;   //!                                                                                                                                                                                                                                  
   TBranch        *b_hlt_mu17_el12;   //!                                                                                                                                                                                                                                    
   TBranch        *b_hlt_mu17_mu8;   //!                                                                                                                                                                                                                                     
   TBranch        *b_hlt_mu17_tkmu8;   //!                                                                                                                                                                                                                                   
   TBranch        *b_hlt_mu8_el17;   //!                                                                                                                                                                                                                                     
   TBranch        *b_nGoodPV;   //!                                                                                                                                                                                                                                          
   TBranch        *b_nPV;   //!                                                                                                                                                                                                                                              
   TBranch        *b_nTrueInteraction;   //!                                                                                                                                                                                                                                 
   TBranch        *b_genWeight;   //!                                                                                                                                                                                                                                        
   TBranch        *b_genWeightQ;   //!                                                                                                                                                                                                                                       
   TBranch        *b_genWeightX1;   //!                                                                                                                                                                                                                                      
   TBranch        *b_genWeightX2;   //!                                                                                                                                                                                                                                      
   TBranch        *b_lheWeight;   //!                                                                                                                                                                                                                                        
   TBranch        *b_puWeight;   //!                                                                                                                                                                                                                                         
   TBranch        *b_puWeightDn;   //!                                                                                                                                                                                                                                       
   TBranch        *b_puWeightUp;   //!                                                                                                                                                                                                                                       
   TBranch        *b_pdfWeight;   //!                                                                                                                                                                                                                                        
   TBranch        *b_triggers_;   //!                                                                                                                                                                                                                                        
   TBranch        *b_triggers_first;   //!                                                                                                                                                                                                                                   
   TBranch        *b_triggers_second;   //!                                                                                                                                                                                                                                  
   TBranch        *b_electrons_absIso03;   //!                                                                                                                                                                                                                               
   TBranch        *b_electrons_absIso04;   //!                                                                                                                                                                                                                               
   TBranch        *b_electrons_chIso03;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_chIso04;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_dxy;   //!                                                                                                                                                                                                                                    
   TBranch        *b_electrons_dz;   //!                                                                                                                                                                                                                                     
   TBranch        *b_electrons_energy;   //!                                                                                                                                                                                                                                 
   TBranch        *b_electrons_eta;   //!                                                                                                                                                                                                                                    
   TBranch        *b_electrons_isGsfCtfScPixChargeConsistent;   //!                                                                                                                                                                                                          
   TBranch        *b_electrons_m;   //!                                                                                                                                                                                                                                      
   TBranch        *b_electrons_nhIso03;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_nhIso04;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_phIso03;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_phIso04;   //!                                                                                                                                                                                                                                
   TBranch        *b_electrons_phi;   //!                                                                                                                                                                                                                                    
   TBranch        *b_electrons_pt;   //!                                                                                                                                                                                                                                     
   TBranch        *b_electrons_puChIso03;   //!                                                                                                                                                                                                                              
   TBranch        *b_electrons_puChIso04;   //!                                                                                                                                                                                                                              
   TBranch        *b_electrons_q;   //!                                                                                                                                                                                                                                      
   TBranch        *b_electrons_relIso03;   //!                                                                                                                                                                                                                               
   TBranch        *b_electrons_relIso04;   //!                                                                                                                                                                                                                               
   TBranch        *b_electrons_scEta;   //!                                                                                                                                                                                                                                  
   TBranch        *b_electrons_shiftedEnDown;   //!                                                                                                                                                                                                                          
   TBranch        *b_electrons_shiftedEnUp;   //!                                                                                                                                                                                                                            
   TBranch        *b_electrons_x;   //!                                                                                                                                                                                                                                      
   TBranch        *b_electrons_y;   //!                                                                                                                                                                                                                                      
   TBranch        *b_electrons_z;   //!                                                                                                                                                                                                                                      
   TBranch        *b_jets_CVSInclV2;   //!                                                                                                                                                                                                                                   
   TBranch        *b_jets_energy;   //!                                                                                                                                                                                                                                      
   TBranch        *b_jets_eta;   //!                                                                                                                                                                                                                                         
   TBranch        *b_jets_isPFId;   //!                                                                                                                                                                                                                                      
   TBranch        *b_jets_m;   //!                                                                                                                                                                                                                                           
   TBranch        *b_jets_phi;   //!                                                                                                                                                                                                                                         
   TBranch        *b_jets_pt;   //!                                                                                                                                                                                                                                          
   TBranch        *b_jets_shiftedEnDown;   //!                                                                                                                                                                                                                               
   TBranch        *b_jets_shiftedEnUp;   //!                                                                                                                                                                                                                                 
   TBranch        *b_jets_smearedRes;   //!                                                                                                                                                                                                                                  
   TBranch        *b_jets_smearedResDown;   //!                                                                                                                                                                                                                              
   TBranch        *b_jets_smearedResUp;   //!                                                                                                                                                                                                                                
   TBranch        *b_jets_vtx3DSig;   //!                                                                                                                                                                                                                                    
   TBranch        *b_jets_vtx3DVal;   //!                                                                                                                                                                                                                                    
   TBranch        *b_jets_vtxMass;   //!                                                                                                                                                                                                                                     
   TBranch        *b_jetsPuppi_CVSInclV2;   //!                                                                                                                                                                                                                              
   TBranch        *b_jetsPuppi_eta;   //!                                                                                                                                                                                                                                    
   TBranch        *b_jetsPuppi_hadronFlavour;   //!                                                                                                                                                                                                                          
   TBranch        *b_jetsPuppi_m;   //!                                                                                                                                                                                                                                      
   TBranch        *b_jetsPuppi_partonFlavour;   //!                                                                                                                                                                                                                          
   TBranch        *b_jetsPuppi_phi;   //!                                                                                                                                                                                                                                    
   TBranch        *b_jetsPuppi_pt;   //!                                                                                                                                                                                                                                     
   TBranch        *b_jetsPuppi_vtx3DSig;   //!                    
   TBranch        *b_jetsPuppi_vtx3DVal;   //!                                                                                                                                                                                                                               
   TBranch        *b_jetsPuppi_vtxMass;   //!                                                                                                                                                                                                                                
   TBranch        *b_met_phi;   //!                                                                                                                                                                                                                                          
   TBranch        *b_met_pt;   //!                                                                                                                                                                                                                                           
   TBranch        *b_met_sumet;   //!                                                                                                                                                                                                                                        
   TBranch        *b_metNoHF_phi;   //!                                                                                                                                                                                                                                      
   TBranch        *b_metNoHF_pt;   //!                                                                                                                                                                                                                                       
   TBranch        *b_metNoHF_sumet;   //!                                                                                                                                                                                                                                    
   TBranch        *b_metPfMva_phi;   //!                                                                                                                                                                                                                                     
   TBranch        *b_metPfMva_pt;   //!                                                                                                                                                                                                                                      
   TBranch        *b_metPfMva_sumet;   //!                                                                                                                                                                                                                                   
   TBranch        *b_metPuppi_phi;   //!                                                                                                                                                                                                                                     
   TBranch        *b_metPuppi_pt;   //!                                                                                                                                                                                                                                      
   TBranch        *b_metPuppi_sumet;   //!                                                                                                                                                                                                                                   
   TBranch        *b_muon_dxy;   //!                                                                                                                                                                                                                                         
   TBranch        *b_muon_dz;   //!                                                                                                                                                                                                                                          
   TBranch        *b_muon_energy;   //!                                                                                                                                                                                                                                      
   TBranch        *b_muon_eta;   //!                                                                                                                                                                                                                                         
   TBranch        *b_muon_m;   //!                                                                                                                                                                                                                                           
   TBranch        *b_muon_normchi;   //!                                                                                                                                                                                                                                     
   TBranch        *b_muon_phi;   //!                                                                                                                                                                                                                                         
   TBranch        *b_muon_pt;   //!                                                                                                                                                                                                                                          
   TBranch        *b_muon_q;   //!                                                                                                                                                                                                                                           
   TBranch        *b_muon_relIso03;   //!                                                                                                                                                                                                                                    
   TBranch        *b_muon_relIso04;   //!                                                                                                                                                                                                                                    
   TBranch        *b_muon_shiftedEdown;   //!                                                                                                                                                                                                                                
   TBranch        *b_muon_shiftedEup;   //!                                                                                                                                                                                                                                  
   TBranch        *b_muon_x;   //!                                                                                                                                                                                                                                           
   TBranch        *b_muon_y;   //!                                                                                                                                                                                                                                           
   TBranch        *b_muon_z;   //!                                                                                                                                                                                                                                           
   TBranch        *b_slimmedGenJets_energy;   //!                                                                                                                                                                                                                            
   TBranch        *b_slimmedGenJets_eta;   //!                                                                                                                                                                                                                               
   TBranch        *b_slimmedGenJets_m;   //!                                                                                                                                                                                                                                 
   TBranch        *b_slimmedGenJets_phi;   //!                                                                                                                                                                                                                               
   TBranch        *b_slimmedGenJets_pt;   //!                                                                                                                                                                                                                                
   TBranch        *b_vertices_ndof;   //!                                                                                                                                                                                                                                    
   TBranch        *b_vertices_x;   //!                                                                                                                                                                                                                                       
   TBranch        *b_vertices_y;   //!                                                                                                                                                                                                                                       
   TBranch        *b_vertices_z;   //!                                                                                                                                                                                                                                       
   TBranch        *b_electrons_electronID_loose;   //!                                                                                                                                                                                                                       
   TBranch        *b_electrons_electronID_medium;   //!          
   TBranch        *b_electrons_electronID_tight;   //!                                                                                                                                                                                                                       
   TBranch        *b_electrons_electronID_veto;   //!                                                                                                                                                                                                                        
   TBranch        *b_electrons_isPF;   //!                                                                                                                                                                                                                                   
   TBranch        *b_electrons_mcMatched;   //!                                                                                                                                                                                                                              
   TBranch        *b_electrons_passConversionVeto;   //!                                                                                                                                                                                                                     
   TBranch        *b_jets_isLoose;   //!                                                                                                                                                                                                                                     
   TBranch        *b_jets_isTight;   //!                                                                                                                                                                                                                                     
   TBranch        *b_jets_isTightLepVetoJetID;   //!                                                                                                                                                                                                                         
   TBranch        *b_muon_isGlobal;   //!                                                                                                                                                                                                                                    
   TBranch        *b_muon_isLoose;   //!                                                                                                                                                                                                                                     
   TBranch        *b_muon_isMedium;   //!                                                                                                                                                                                                                                    
   TBranch        *b_muon_isPF;   //!                                                                                                                                                                                                                                        
   TBranch        *b_muon_isSoft;   //!                                                                                                                                                                                                                                      
   TBranch        *b_muon_isTight;   //!                                                                                                                                                                                                                                     
   TBranch        *b_muon_isTracker;   //!                                                                                                                                                                                                                                   
   TBranch        *b_muon_matched;   //!                                                                                                                                                                                                                                     
   TBranch        *b_electrons_electronID_snu;   //!                                                                                                                                                                                                                         
   TBranch        *b_jets_hadronFlavour;   //!                                                                                                                                                                                                                               
   TBranch        *b_jets_partonFlavour;   //!                                                                                                                                                                                                                               
   TBranch        *b_jets_partonPdgId;   //!                                                                                                                                                                                                                                 
   TBranch        *b_jets_vtxNtracks;   //!                                                                                                                                                                                                                                  
   TBranch        *b_muon_matchedstations;   //!                                                                                                                                                                                                                             
   TBranch        *b_muon_trackerlayers;   //!                                                                                                                                                                                                                               
   TBranch        *b_muon_validhits;   //!                                                                                                                                                                                                                                   
   TBranch        *b_muon_validmuonhits;   //!                                                                                                                                                                                                                               
   TBranch        *b_muon_validpixhits;   //!     


   TBranch        *b_inputmuons;
   TBranch        *b_inputtrigger;
   TBranch        *b_inputtruth;
   TBranch        *b_inputjets;
   TBranch        *b_inputgenjets;
   TBranch        *b_inputevent;
   TBranch        *b_inputelectrons;



};

#endif
