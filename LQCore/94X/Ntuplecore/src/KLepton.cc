// LOCAL includes
#include "KLepton.h"

// STL
#include <sstream>

// ROOT

KLepton::KLepton() :
  KParticle(),
  k_flavour(KLepton::NOTSET),
  k_dz(-999),
  k_ip2d(-999),
  k_sip3d(-999),
  k_reliso(-999),
  k_leptype(-999),
  k_mciscf(false),
  MuonPtr(NULL),
  ElectronPtr(NULL)
{

}

KLepton::KLepton(const KLepton& lep) :
  KParticle(lep),
  k_flavour(lep.LeptonFlavour()),
  k_dz(lep.dZ()),
  k_ip2d(lep.IP2D()),
  k_sip3d(lep.SIP3D()),
  k_reliso(lep.RelIso()),
  k_leptype(lep.GetType()),
  k_mciscf(lep.MCIsCF())
{
  if(k_flavour==KLepton::MUON) MuonPtr = lep.MuonPtr;
  if(k_flavour==KLepton::ELECTRON) ElectronPtr = lep.ElectronPtr;
}

KLepton::KLepton(const snu::KMuon& muon) :
  KParticle(muon),
  k_flavour(KLepton::MUON),
  k_dz(muon.dZ()),
  k_ip2d(muon.IP2D()),
  k_sip3d(muon.SIP3D()),
  k_reliso(muon.RelIso04()),
  k_leptype(muon.GetType()),
  k_mciscf(muon.MCIsCF()),
  MuonPtr(&muon),
  ElectronPtr(NULL)
{

}

KLepton::KLepton(const snu::KElectron& electron) :
  KParticle(electron),
  k_flavour(KLepton::ELECTRON),
  k_dz(electron.dz()),
  k_ip2d(electron.IP2D()),
  k_sip3d(electron.SIP3D()),
  k_reliso(electron.PFRelIsoBeta(0.3)),
  k_leptype(electron.GetType()),
  k_mciscf(electron.MCIsCF()),
  MuonPtr(NULL),
  ElectronPtr(&electron)
{

}

KLepton::~KLepton(){

}

KLepton& KLepton::operator= (const KLepton& lep){

  if(this != &lep){
    KParticle::operator=(lep);
    k_flavour = lep.k_flavour;
    k_dz = lep.k_dz;
    k_ip2d = lep.k_ip2d;
    k_sip3d = lep.k_sip3d;
    k_reliso = lep.k_reliso;
    k_leptype = lep.k_leptype;
    k_mciscf = lep.k_mciscf;
    MuonPtr = lep.MuonPtr;
    ElectronPtr = lep.ElectronPtr;
  }  

  return *this;

}

KLepton& KLepton::operator= (const snu::KMuon& muon){

  KParticle::operator=(muon);
  k_flavour = KLepton::MUON;
  k_dz = muon.dZ();
  k_ip2d = muon.IP2D();
  k_sip3d = muon.SIP3D();
  k_reliso = muon.RelIso04();
  k_leptype = muon.GetType();
  k_mciscf = muon.MCIsCF();
  MuonPtr = &muon;
  ElectronPtr = NULL;

  return *this;

}

KLepton& KLepton::operator= (const snu::KElectron& electron){

  KParticle::operator=(electron);
  k_flavour = KLepton::ELECTRON;
  k_dz = electron.dz();
  k_ip2d = electron.IP2D();
  k_sip3d = electron.SIP3D();
  k_reliso = electron.PFRelIsoBeta(0.3);
  k_leptype = electron.GetType();
  k_mciscf = electron.MCIsCF();
  MuonPtr = NULL;
  ElectronPtr = &electron;

  return *this;

}

//==== FIXME
/*
template <typename T>
T KLepton::GetLeptonPtr(){

  if(MuonPtr) return MuonPtr;
  if(ElectronPtr) return ElectronPtr;
  return NULL;

}
*/







