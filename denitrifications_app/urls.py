from django.urls import path
from . import views
app_name = "denitrifications_app"

urlpatterns = [
    path('', views.home, name='home'),
    #------------------------------------Enzymes--------------------------------
    path('NarG/',views.NarG,name="NarG"),
    path('NarG/<int:page>',views.NarG,name="NarG"),
    path('NarG/<str:opt>/<str:inputText>/<int:page>',views.NarG,name="NarG"),
    
    
    path('NapA/', views.NapA, name="NapA"),
    path('NapA/<int:page>/', views.NapA, name="NapA"),
    path('NapA/<str:opt>/<str:inputText>/<int:page>', views.NapA, name="NapA"),

    
    path('NirK/',views.NirK, name="NirK"),
    path('NirK/<int:page>',views.NirK, name="NirK"),
    path('NirK/<str:opt>/<str:inputText>/<int:page>',views.NirK,name="NirK"),
    
    path('NirS/',views.NirS,name="NirS"),
    path('NirS/<int:page>',views.NirS,name="NirS"),
    path('NirS/<str:opt>/<str:inputText>/<int:page>',views.NirS,name="NirS"),
    
    path('cNorB/', views.cNorB, name="cNorB"),
    path('cNorB/<int:page>', views.cNorB, name="cNorB"),
    path('cNorB/<str:opt>/<str:inputText>/<int:page>',views.cNorB,name="cNorB"),
    
    path('qNorB/',views.qNorB, name="qNorB"),
    path('qNorB/<int:page>',views.qNorB, name="qNorB"),
    path('qNorB/<str:opt>/<str:inputText>/<int:page>',views.qNorB,name="qNorB"),
    
    path('NosZ/',views.NosZ, name="NosZ"),
    path('NosZ/<int:page>',views.NosZ, name="NosZ"),
    path('NosZ/<str:opt>/<str:inputText>/<int:page>',views.NosZ,name="NosZ"),
    
    
    path("EnzymesDetail/<str:EnzymeName>/<str:GenBank_ID>/", views.EnzymesDetail, name="EnzymesDetail"),
    # ------------------------------------products--------------------------------
    path('Strains/', views.Product, name = "Strains"),
    path('Strains/<int:page>/', views.Product, name = "Product"),
    path('Strains/<str:Accession_num>/', views.product_detail, name = "Strains"),
    
    path('Microorganism/', views.productMicro, name = "Microorganism"),
    path('Microorganism/<str:inputText>/<int:page>/', views.productMicro, name = "Microorganism"),
    path('Microorganism/<str:opt>/<str:inputText>/<int:page>/', views.productMicro, name = "Microorganism"),
    
    # ------------------------------------test------------------------------------
    path('add/', views.add, name = "add"),
    # ------------------------------------pathway-----------------------------------
    #path("Pathway/", views.pathway, name="Pathway"),
    path("path_svg/", views.path_svg, name="Pathway"),
    
    # ------------------------------------Prediction--------------------------------
    path("Prediction/", views.prediction, name="Prediction"),
    path("hmmer/", views.hmmer, name = "hmmer"),
    path("blast/", views.blast, name = "blast"),
    path("clusto/", views.clusto, name = "clusto"),
    path("Paste/", views.paste, name = "Paste"),

    path("download/", views.download, name = "download"),
    path("Upload/", views.upload, name = "Upload"),
    path("IDSearch/", views.idsearch, name = "IDSearch"),
    path("downloadSeq/", views.downloadSeq, name = "downloadSeq"),
    path("BlastPaste/",views.blastpaste, name = "BlastPaste"),
    path("BlastUpload/", views.blastupload, name = "BlastUpload"),

    path("phylotree/", views.phylotree, name="phylotree"),
    
    # ------------------------------------Rectation---------------------------------
    path("Enzyme/", views.enzyme, name="Enzyme"),
    path("Enzyme_Narg/", views.enzyme_narg, name="Enzyme_Narg"),
    path("Enzyme_Napa/", views.enzyme_napa, name="Enzyme_Napa"),
    path("Enzyme_Nirk/", views.enzyme_nirk, name="Enzyme_Nirk"),
    path("Enzyme_Nirs/", views.enzyme_nirs, name="Enzyme_Nirs"),
    path("Enzyme_Norc/", views.enzyme_norc, name="Enzyme_Norc"),
    path("Enzyme_Norb/", views.enzyme_norb, name="Enzyme_Norb"),
    path("Enzyme_Nosz/", views.enzyme_nosz, name="Enzyme_Nosz"),
    path("Mechanism/", views.mechanism, name="Mechanism"),
    path("NitrateReduction/<int:num>/", views.nitrate_reduction, name="NitrateReduction"),

    # ----------------------------------Denitrification System-----------------------
    path("WastewaterTreat/", views.WastewaterTreat, name = "WastewaterTreat"),
    path("WastewaterTreat/<int:page>", views.WastewaterTreat, name = "WastewaterTreat"),
    
    path("FreshwaterSystems/", views.FreshwaterSystems, name = "FreshwaterSystems"),
    path("FreshwaterSystems/<int:page>/", views.FreshwaterSystems, name = "FreshwaterSystems"),
    
    path("MarineSystems/", views.MarineSystems, name = "MarineSystems"),
    path("MarineSystems/<int:page>/", views.MarineSystems, name = "MarineSystems"),
    
    path("GroundwaterSystems/", views.GroundwaterSystems, name = "GroundwaterSystems"),
    path("GroundwaterSystems/<int:page>/", views.GroundwaterSystems, name = "GroundwaterSystems"),
    
    path("WetlandsRiparinZones/", views.WetlandsRiparinZone, name="WetlandsRiparinZones"),
    path("WetlandsRiparinZones/<int:page>/", views.WetlandsRiparinZone, name = "WetlandsRiparinZones"),
    
    path("SulphurRemoval/", views.sulphurRemoval, name = "SulphurRemoval"),
    path("SulphurRemoval/<int:page>/", views.sulphurRemoval, name = "SulphurRemoval"),

    # ---------------------------------Bioreactor------------------------------------------
    path("FluidizedBedReactors/", views.FluidizedBedReactors, name = "FluidizedBedReactors"),
    path("ContinuousStirredTankReactor/", views.ContinuousStirredTankReactor, name = "ContinuousStirredTankReactor"),
    path("MovingBedBiofilmReactor/", views.MovingBedBiofilmReactor, name = "MovingBedBiofilmReactor"),
    path("PackedBedReactor/", views.PackedBedReactor, name = "PackedBedReactor"),
    path("MembraneBioreactor/", views.MembraneBioreactor, name = "MembraneBioreactor"),
    path("SequencingBatchBioreactor/", views.SequencingBatchBioreactor, name = "SequencingBatchBioreactor"),

    # ---------------------------------------about-----------------------------------
    path("about/", views.about, name = "about"),

    # ---------------------------------submit----------------------------------------------
    path("submit/", views.submit, name = "submit"),

    # ---------------------------------contact----------------------------------------------
    path("contact/", views.contact, name = "contact"),

    # ----------------------------------Download inofrmation-------------------------------
    path("download/", views.download, name = "download"),
    path("DownloadGenes/", views.downloadGenes, name = "DownloadGenes"),
    path("DownloadStrains/", views.downloadStrains, name = "DownloadStrains"),
    path("DownloadSequence/", views.downloadSequence, name = "DownloadSequence"),
    path("DownloadDenitriSystem/", views.downloadDenitriSystem, name="DownloadDenitriSystem"),
    path("DownloadBioreactor/", views.downloadBioreactor, name="DownloadBioreactor"),
]