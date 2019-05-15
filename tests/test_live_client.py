#!/usr/bin/python
# -*- coding: utf-8 -*-

# © Copyright 2019 CERN
#
# This software is distributed under the terms of the GNU General Public
# Licence version 3 (GPL Version 3), copied verbatim in the file “LICENSE”
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.
import pytest

import runreg


def test_get_multiple_pages():
    runs = runreg.get(run_number=[(327744, "<="), (327030, ">=")])
    count = len(runs)
    assert 75 <= count <= 100


def test_get_flat():
    runs = runreg.get(flat=True, run_number=(327596, "="))
    run = runs[0]

    expected_keys = [
        "id",
        "name",
        "appeared_in__by",
        "appeared_in__when",
        "appeared_in__value",
        "global_state__by",
        "global_state__when",
        "global_state__value",
        "btag_state__by",
        "btag_state__when",
        "btag_state__value",
        "btag-btag__by",
        "btag-btag__when",
        "btag-btag__cause",
        "btag-btag__status",
        "btag-btag__comment",
        "castor_state__by",
        "castor_state__when",
        "castor_state__value",
        "castor-castor__by",
        "castor-castor__when",
        "castor-castor__cause",
        "castor-castor__status",
        "castor-castor__comment",
        "csc_state__by",
        "csc_state__when",
        "csc_state__value",
        "csc-csc__by",
        "csc-csc__when",
        "csc-csc__cause",
        "csc-csc__status",
        "csc-csc__comment",
        "csc-occupancy__by",
        "csc-occupancy__when",
        "csc-occupancy__cause",
        "csc-occupancy__status",
        "csc-occupancy__comment",
        "csc-integrity__by",
        "csc-integrity__when",
        "csc-integrity__cause",
        "csc-integrity__status",
        "csc-integrity__comment",
        "csc-strips__by",
        "csc-strips__when",
        "csc-strips__cause",
        "csc-strips__status",
        "csc-strips__comment",
        "csc-timing__by",
        "csc-timing__when",
        "csc-timing__cause",
        "csc-timing__status",
        "csc-timing__comment",
        "csc-efficiency__by",
        "csc-efficiency__when",
        "csc-efficiency__cause",
        "csc-efficiency__status",
        "csc-efficiency__comment",
        "csc-gasgains__by",
        "csc-gasgains__when",
        "csc-gasgains__cause",
        "csc-gasgains__status",
        "csc-gasgains__comment",
        "csc-pedestals__by",
        "csc-pedestals__when",
        "csc-pedestals__cause",
        "csc-pedestals__status",
        "csc-pedestals__comment",
        "csc-resolution__by",
        "csc-resolution__when",
        "csc-resolution__cause",
        "csc-resolution__status",
        "csc-resolution__comment",
        "csc-segments__by",
        "csc-segments__when",
        "csc-segments__cause",
        "csc-segments__status",
        "csc-segments__comment",
        "csc-tf__by",
        "csc-tf__when",
        "csc-tf__cause",
        "csc-tf__status",
        "csc-tf__comment",
        "csc-triggergpe__by",
        "csc-triggergpe__when",
        "csc-triggergpe__cause",
        "csc-triggergpe__status",
        "csc-triggergpe__comment",
        "ctpps_state__by",
        "ctpps_state__when",
        "ctpps_state__value",
        "ctpps-ctpps__by",
        "ctpps-ctpps__when",
        "ctpps-ctpps__cause",
        "ctpps-ctpps__status",
        "ctpps-ctpps__comment",
        "ctpps-rp45_210__by",
        "ctpps-rp45_210__when",
        "ctpps-rp45_210__cause",
        "ctpps-rp45_210__status",
        "ctpps-rp45_210__comment",
        "ctpps-rp45_220__by",
        "ctpps-rp45_220__when",
        "ctpps-rp45_220__cause",
        "ctpps-rp45_220__status",
        "ctpps-rp45_220__comment",
        "ctpps-rp45_cyl__by",
        "ctpps-rp45_cyl__when",
        "ctpps-rp45_cyl__cause",
        "ctpps-rp45_cyl__status",
        "ctpps-rp45_cyl__comment",
        "ctpps-rp56_210__by",
        "ctpps-rp56_210__when",
        "ctpps-rp56_210__cause",
        "ctpps-rp56_210__status",
        "ctpps-rp56_210__comment",
        "ctpps-rp56_220__by",
        "ctpps-rp56_220__when",
        "ctpps-rp56_220__cause",
        "ctpps-rp56_220__status",
        "ctpps-rp56_220__comment",
        "ctpps-rp56_cyl__by",
        "ctpps-rp56_cyl__when",
        "ctpps-rp56_cyl__cause",
        "ctpps-rp56_cyl__status",
        "ctpps-rp56_cyl__comment",
        "ctpps-trk45_210__by",
        "ctpps-trk45_210__when",
        "ctpps-trk45_210__cause",
        "ctpps-trk45_210__status",
        "ctpps-trk45_210__comment",
        "ctpps-time45__by",
        "ctpps-time45__when",
        "ctpps-time45__cause",
        "ctpps-time45__status",
        "ctpps-time45__comment",
        "ctpps-trk56_220__by",
        "ctpps-trk56_220__when",
        "ctpps-trk56_220__cause",
        "ctpps-trk56_220__status",
        "ctpps-trk56_220__comment",
        "ctpps-time56__by",
        "ctpps-time56__when",
        "ctpps-time56__cause",
        "ctpps-time56__status",
        "ctpps-time56__comment",
        "ctpps-time_global__by",
        "ctpps-time_global__when",
        "ctpps-time_global__cause",
        "ctpps-time_global__status",
        "ctpps-time_global__comment",
        "dt_state__by",
        "dt_state__when",
        "dt_state__value",
        "dt-dt__by",
        "dt-dt__when",
        "dt-dt__cause",
        "dt-dt__status",
        "dt-dt__comment",
        "ecal_state__by",
        "ecal_state__when",
        "ecal_state__value",
        "ecal-ecal__by",
        "ecal-ecal__when",
        "ecal-ecal__cause",
        "ecal-ecal__status",
        "ecal-ecal__comment",
        "ecal-ebp__by",
        "ecal-ebp__when",
        "ecal-ebp__cause",
        "ecal-ebp__status",
        "ecal-ebp__comment",
        "ecal-ebm__by",
        "ecal-ebm__when",
        "ecal-ebm__cause",
        "ecal-ebm__status",
        "ecal-ebm__comment",
        "ecal-eep__by",
        "ecal-eep__when",
        "ecal-eep__cause",
        "ecal-eep__status",
        "ecal-eep__comment",
        "ecal-eem__by",
        "ecal-eem__when",
        "ecal-eem__cause",
        "ecal-eem__status",
        "ecal-eem__comment",
        "ecal-es__by",
        "ecal-es__when",
        "ecal-es__cause",
        "ecal-es__status",
        "ecal-es__comment",
        "ecal-esp__by",
        "ecal-esp__when",
        "ecal-esp__cause",
        "ecal-esp__status",
        "ecal-esp__comment",
        "ecal-esm__by",
        "ecal-esm__when",
        "ecal-esm__cause",
        "ecal-esm__status",
        "ecal-esm__comment",
        "ecal-analysis__by",
        "ecal-analysis__when",
        "ecal-analysis__cause",
        "ecal-analysis__status",
        "ecal-analysis__comment",
        "ecal-collisions__by",
        "ecal-collisions__when",
        "ecal-collisions__cause",
        "ecal-collisions__status",
        "ecal-collisions__comment",
        "ecal-laser__by",
        "ecal-laser__when",
        "ecal-laser__cause",
        "ecal-laser__status",
        "ecal-laser__comment",
        "ecal-tpg__by",
        "ecal-tpg__when",
        "ecal-tpg__cause",
        "ecal-tpg__status",
        "ecal-tpg__comment",
        "ecal-noise__by",
        "ecal-noise__when",
        "ecal-noise__cause",
        "ecal-noise__status",
        "ecal-noise__comment",
        "ecal-preshower__by",
        "ecal-preshower__when",
        "ecal-preshower__cause",
        "ecal-preshower__status",
        "ecal-preshower__comment",
        "ecal-timing__by",
        "ecal-timing__when",
        "ecal-timing__cause",
        "ecal-timing__status",
        "ecal-timing__comment",
        "egamma_state__by",
        "egamma_state__when",
        "egamma_state__value",
        "egamma-egamma__by",
        "egamma-egamma__when",
        "egamma-egamma__cause",
        "egamma-egamma__status",
        "egamma-egamma__comment",
        "hcal_state__by",
        "hcal_state__when",
        "hcal_state__value",
        "hcal-hb__by",
        "hcal-hb__when",
        "hcal-hb__cause",
        "hcal-hb__status",
        "hcal-hb__comment",
        "hcal-he__by",
        "hcal-he__when",
        "hcal-he__cause",
        "hcal-he__status",
        "hcal-he__comment",
        "hcal-hf__by",
        "hcal-hf__when",
        "hcal-hf__cause",
        "hcal-hf__status",
        "hcal-hf__comment",
        "hcal-ho0__by",
        "hcal-ho0__when",
        "hcal-ho0__cause",
        "hcal-ho0__status",
        "hcal-ho0__comment",
        "hcal-ho12__by",
        "hcal-ho12__when",
        "hcal-ho12__cause",
        "hcal-ho12__status",
        "hcal-ho12__comment",
        "hlt_state__by",
        "hlt_state__when",
        "hlt_state__value",
        "hlt-muons__by",
        "hlt-muons__when",
        "hlt-muons__cause",
        "hlt-muons__status",
        "hlt-muons__comment",
        "hlt-electrons__by",
        "hlt-electrons__when",
        "hlt-electrons__cause",
        "hlt-electrons__status",
        "hlt-electrons__comment",
        "hlt-photons__by",
        "hlt-photons__when",
        "hlt-photons__cause",
        "hlt-photons__status",
        "hlt-photons__comment",
        "hlt-jetmet__by",
        "hlt-jetmet__when",
        "hlt-jetmet__cause",
        "hlt-jetmet__status",
        "hlt-jetmet__comment",
        "hlt-tau__by",
        "hlt-tau__when",
        "hlt-tau__cause",
        "hlt-tau__status",
        "hlt-tau__comment",
        "hlt-bjets__by",
        "hlt-bjets__when",
        "hlt-bjets__cause",
        "hlt-bjets__status",
        "hlt-bjets__comment",
        "hlt-technical__by",
        "hlt-technical__when",
        "hlt-technical__cause",
        "hlt-technical__status",
        "hlt-technical__comment",
        "jetmet_state__by",
        "jetmet_state__when",
        "jetmet_state__value",
        "jetmet-jetmet__by",
        "jetmet-jetmet__when",
        "jetmet-jetmet__cause",
        "jetmet-jetmet__status",
        "jetmet-jetmet__comment",
        "l1t_state__by",
        "l1t_state__when",
        "l1t_state__value",
        "l1t-l1tmu__by",
        "l1t-l1tmu__when",
        "l1t-l1tmu__cause",
        "l1t-l1tmu__status",
        "l1t-l1tmu__comment",
        "l1t-l1tcalo__by",
        "l1t-l1tcalo__when",
        "l1t-l1tcalo__cause",
        "l1t-l1tcalo__status",
        "l1t-l1tcalo__comment",
        "l1t-software__by",
        "l1t-software__when",
        "l1t-software__cause",
        "l1t-software__status",
        "l1t-software__comment",
        "lumi_state__by",
        "lumi_state__when",
        "lumi_state__value",
        "lumi-lumi__by",
        "lumi-lumi__when",
        "lumi-lumi__cause",
        "lumi-lumi__status",
        "lumi-lumi__comment",
        "muon_state__by",
        "muon_state__when",
        "muon_state__value",
        "muon-muon__by",
        "muon-muon__when",
        "muon-muon__cause",
        "muon-muon__status",
        "muon-muon__comment",
        "rpc_state__by",
        "rpc_state__when",
        "rpc_state__value",
        "rpc-rpc__by",
        "rpc-rpc__when",
        "rpc-rpc__cause",
        "rpc-rpc__status",
        "rpc-rpc__comment",
        "rpc-hv__by",
        "rpc-hv__when",
        "rpc-hv__cause",
        "rpc-hv__status",
        "rpc-hv__comment",
        "rpc-lv__by",
        "rpc-lv__when",
        "rpc-lv__cause",
        "rpc-lv__status",
        "rpc-lv__comment",
        "rpc-feb__by",
        "rpc-feb__when",
        "rpc-feb__cause",
        "rpc-feb__status",
        "rpc-feb__comment",
        "rpc-noise__by",
        "rpc-noise__when",
        "rpc-noise__cause",
        "rpc-noise__status",
        "rpc-noise__comment",
        "rpc-elog__by",
        "rpc-elog__when",
        "rpc-elog__cause",
        "rpc-elog__status",
        "rpc-elog__comment",
        "tau_state__by",
        "tau_state__when",
        "tau_state__value",
        "tau-tau__by",
        "tau-tau__when",
        "tau-tau__cause",
        "tau-tau__status",
        "tau-tau__comment",
        "tracker_state__by",
        "tracker_state__when",
        "tracker_state__value",
        "tracker-track__by",
        "tracker-track__when",
        "tracker-track__cause",
        "tracker-track__status",
        "tracker-track__comment",
        "tracker-pix__by",
        "tracker-pix__when",
        "tracker-pix__cause",
        "tracker-pix__status",
        "tracker-pix__comment",
        "tracker-strip__by",
        "tracker-strip__when",
        "tracker-strip__cause",
        "tracker-strip__status",
        "tracker-strip__comment",
        "btag__by",
        "btag__when",
        "btag__cause",
        "btag__status",
        "btag__comment",
        "castor__by",
        "castor__when",
        "castor__cause",
        "castor__status",
        "castor__comment",
        "cms__by",
        "cms__when",
        "cms__cause",
        "cms__status",
        "cms__comment",
        "csc__by",
        "csc__when",
        "csc__cause",
        "csc__status",
        "csc__comment",
        "ctpps__by",
        "ctpps__when",
        "ctpps__cause",
        "ctpps__status",
        "ctpps__comment",
        "dt__by",
        "dt__when",
        "dt__cause",
        "dt__status",
        "dt__comment",
        "ecal__by",
        "ecal__when",
        "ecal__cause",
        "ecal__status",
        "ecal__comment",
        "egamma__by",
        "egamma__when",
        "egamma__cause",
        "egamma__status",
        "egamma__comment",
        "es__by",
        "es__when",
        "es__cause",
        "es__status",
        "es__comment",
        "hcal__by",
        "hcal__when",
        "hcal__cause",
        "hcal__status",
        "hcal__comment",
        "hlt__by",
        "hlt__when",
        "hlt__cause",
        "hlt__status",
        "hlt__comment",
        "jetmet__by",
        "jetmet__when",
        "jetmet__cause",
        "jetmet__status",
        "jetmet__comment",
        "l1t__by",
        "l1t__when",
        "l1t__cause",
        "l1t__status",
        "l1t__comment",
        "l1tcalo__by",
        "l1tcalo__when",
        "l1tcalo__cause",
        "l1tcalo__status",
        "l1tcalo__comment",
        "l1tmu__by",
        "l1tmu__when",
        "l1tmu__cause",
        "l1tmu__status",
        "l1tmu__comment",
        "lowLumi__by",
        "lowLumi__when",
        "lowLumi__cause",
        "lowLumi__status",
        "lowLumi__comment",
        "lumi__by",
        "lumi__when",
        "lumi__cause",
        "lumi__status",
        "lumi__comment",
        "muon__by",
        "muon__when",
        "muon__cause",
        "muon__status",
        "muon__comment",
        "pix__by",
        "pix__when",
        "pix__cause",
        "pix__status",
        "pix__comment",
        "rpc__by",
        "rpc__when",
        "rpc__cause",
        "rpc__status",
        "rpc__comment",
        "strip__by",
        "strip__when",
        "strip__cause",
        "strip__status",
        "strip__comment",
        "tau__by",
        "tau__when",
        "tau__cause",
        "tau__status",
        "tau__comment",
        "track__by",
        "track__when",
        "track__cause",
        "track__status",
        "track__comment",
        "createdAt",
        "updatedAt",
        "run_number",
        "run__class__by",
        "run__class__when",
        "run__class__value",
        "run__state__by",
        "run__state__when",
        "run__state__value",
        "run__significant__by",
        "run__significant__when",
        "run__significant__value",
        "run__stop_reason__by",
        "run__stop_reason__when",
        "run__stop_reason__value",
    ]
    assert set(expected_keys) == set(run.keys())

    assert run["run_number"] == 327596
    assert run["run__class__value"] == "Cosmics18"
    assert run["name"] == "/PromptReco/HICosmics18A/DQM"


def test_get():
    runs = runreg.get(run_number=327596)
    run = runs[0]

    expected_keys = [
        "id",
        "name",
        "appeared_in",
        "global_state",
        "global_lumisections",
        "btag_state",
        "btag_lumisections",
        "btag-btag",
        "castor_state",
        "castor_lumisections",
        "castor-castor",
        "csc_state",
        "csc_lumisections",
        "csc-csc",
        "csc-occupancy",
        "csc-integrity",
        "csc-strips",
        "csc-timing",
        "csc-efficiency",
        "csc-gasgains",
        "csc-pedestals",
        "csc-resolution",
        "csc-segments",
        "csc-tf",
        "csc-triggergpe",
        "ctpps_state",
        "ctpps_lumisections",
        "ctpps-ctpps",
        "ctpps-rp45_210",
        "ctpps-rp45_220",
        "ctpps-rp45_cyl",
        "ctpps-rp56_210",
        "ctpps-rp56_220",
        "ctpps-rp56_cyl",
        "ctpps-trk45_210",
        "ctpps-time45",
        "ctpps-trk56_220",
        "ctpps-time56",
        "ctpps-time_global",
        "dt_state",
        "dt_lumisections",
        "dt-dt",
        "ecal_state",
        "ecal_lumisections",
        "ecal-ecal",
        "ecal-ebp",
        "ecal-ebm",
        "ecal-eep",
        "ecal-eem",
        "ecal-es",
        "ecal-esp",
        "ecal-esm",
        "ecal-analysis",
        "ecal-collisions",
        "ecal-laser",
        "ecal-tpg",
        "ecal-noise",
        "ecal-preshower",
        "ecal-timing",
        "egamma_state",
        "egamma_lumisections",
        "egamma-egamma",
        "hcal_state",
        "hcal_lumisections",
        "hcal-hb",
        "hcal-he",
        "hcal-hf",
        "hcal-ho0",
        "hcal-ho12",
        "hlt_state",
        "hlt_lumisections",
        "hlt-muons",
        "hlt-electrons",
        "hlt-photons",
        "hlt-jetmet",
        "hlt-tau",
        "hlt-bjets",
        "hlt-technical",
        "jetmet_state",
        "jetmet_lumisections",
        "jetmet-jetmet",
        "l1t_state",
        "l1t_lumisections",
        "l1t-l1tmu",
        "l1t-l1tcalo",
        "l1t-software",
        "lumi_state",
        "lumi_lumisections",
        "lumi-lumi",
        "muon_state",
        "muon_lumisections",
        "muon-muon",
        "rpc_state",
        "rpc_lumisections",
        "rpc-rpc",
        "rpc-hv",
        "rpc-lv",
        "rpc-feb",
        "rpc-noise",
        "rpc-elog",
        "tau_state",
        "tau_lumisections",
        "tau-tau",
        "tracker_state",
        "tracker_lumisections",
        "tracker-track",
        "tracker-pix",
        "tracker-strip",
        "btag",
        "castor",
        "cms",
        "csc",
        "ctpps",
        "dt",
        "ecal",
        "egamma",
        "es",
        "hcal",
        "hlt",
        "jetmet",
        "l1t",
        "l1tcalo",
        "l1tmu",
        "lowLumi",
        "lumi",
        "muon",
        "pix",
        "rpc",
        "strip",
        "tau",
        "track",
        "createdAt",
        "updatedAt",
        "run_number",
        "run",
    ]
    assert set(expected_keys) == set(run.keys())

    assert run["run_number"] == 327596
    assert run["name"] == "/PromptReco/HICosmics18A/DQM"
    assert run["run"]["class"]["value"] == "Cosmics18"
    assert "status" in run["strip"]
    assert "status" in run["pix"]
    assert "status" in run["track"]


def test_get_with_lookup_field():
    runs = runreg.get(run_number__eq=327596)
    run = runs[0]
    assert run["run_number"] == 327596
    assert run["name"] == "/PromptReco/HICosmics18A/DQM"
    assert run["run"]["class"]["value"] == "Cosmics18"
    assert "status" in run["strip"]
    assert "status" in run["pix"]
    assert "status" in run["track"]


def test_get_with_multiple_lookup_fields():
    runs = runreg.get(run_number__lte=327744, run_number__gte=327033)
    count = len(runs)
    assert 75 <= count <= 100


def test_get_incorrect_parameters():
    with pytest.raises(ValueError):
        runreg.get(this_does_not_exist=1234)
