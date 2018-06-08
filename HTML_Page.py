# -*- coding: utf-8 -*-
import os

class HTML_Page(object):
    """docstring for HTML_Page"""
    def __init__(self):
        return

    def print_html(self, path, name, title, polyline, lat_init, lng_init, lat_fim, lng_fim, distance, time_of_trip, timestamp, traffic, dist):

        file = name
        filename = file + ".html"
        # filepath = os.path.join(path, filename)
        filename = path + filename
        f = open(filename,"w")

        f.write("<html>")

        f.write("<head>")

        f.write("""<style type="text/css">
            .gm-style .gm-style-mtc label,
            .gm-style .gm-style-mtc div {
                font-weight: 400
            }
        </style>
        <link type="text/css" rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700">
        <style type="text/css">
            .gm-style .gm-style-cc span,
            .gm-style .gm-style-cc a,
            .gm-style .gm-style-mtc div {
                font-size: 10px
            }
        </style>
        <style type="text/css">
            @media print {
                .gm-style .gmnoprint,
                .gmnoprint {
                    display: none
                }
            }

            @media screen {
                .gm-style .gmnoscreen,
                .gmnoscreen {
                    display: none
                }
            }
        </style>""")

        f.write("""
            <style type="text/css">
            .gm-style-pbc {
                transition: opacity ease-in-out;
                background-color: rgba(0, 0, 0, 0.45);
                text-align: center
            }

            .gm-style-pbt {
                font-size: 22px;
                color: white;
                font-family: Roboto, Arial, sans-serif;
                position: relative;
                margin: 0;
                top: 50%;
                -webkit-transform: translateY(-50%);
                -ms-transform: translateY(-50%);
                transform: translateY(-50%)
            }
        </style> """)

        # title = "Estrada_Ribeira_TO_Av_Rui_Barbosa_1"
        f.write("<title>" + title + "</title>")

        f.write(""" <script type="text/javascript" src="http://maps.google.com/maps/api/js?libraries=geometry&amp;sensor=false"></script> """)
        f.write(""" <style type="text/css">
            #map {
                width: 670px;
                height: 600px;
            }
        </style> """)

        f.write(""" <script type="text/javascript"> """)
        f.write(""" function initialize() { """)
        lat, lng = -22.907104, -47.063240

        f.write("var myLatlng = new google.maps.LatLng(" + str(lat) + "," + str(lng) + ");")
        f.write("""  var myOptions = {
                    zoom: 11,
                    center: myLatlng,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                }
                var map = new google.maps.Map(document.getElementById("map"), myOptions); """)

        f.write("var decodedPath = google.maps.geometry.encoding.decodePath(")
        # polyline =""" 'j_vyCdjakHh@jALNz@lBZx@Rx@Dd@@z@Ej@g@jCMh@o@xAk@nCsA~Gg@fCsBzJi@xCKhB@l@HjAVrAv@lBt@|@j@j@`F~EdCdCxFrFl@l@|BvBb@Xd@RnDv@hF`A~TjE|AZ|@\\n@`@`DbDpDrDlChCzAdAfDzBjAp@f@XtAv@|DdC~GpEdBfAxDbC|EbDpExCvBvA`FbDpDfCjCpBzF|EtKzIxWrT|SdQvC`ChCtBpBdBxD|C|BlBr@`ArA|Ap@f@nFnEdDjC|@v@jAx@fEhDxDdDrAfAVNZJNBJJb@`@`BrBlFvHrAnBr@~@^`@zAtAfBlAt@^hFjBnE|A~OtFvOpFrKlDjJdDxKtDfL~DfA`@zGxB`FhBbEtAzKzDrC~@dJdDrQ|FtPvFdBf@z@\\|JlDt@ZbBp@z@j@h@^^^xAlBtAnBHFlCzDz@hA|@`AdAx@lAh@v@Rv@LfADtAExIu@fCO|D@jAB|AClBApA@lAB`@@r@F~AVbBHNBtBb@Xd@FX@VEd@I~ABlAETILKDS@OGSYQ_@OyCIyC@UFc@Ng@Za@j@i@xGaFtEkDdEyC~@w@nDoCxEeDtB{AxC{Bp@g@~PiMhDoC`FqDhPuLvOmLhIeGtC}BjEaD~KiItImG`CmB~KmIrKaIfCsBdBeBvBiCfBoCz@{ApAqC`AeCxD}KZ_A|CgJzB}GtLg]rLs]`Xaw@bMq^lHiTjD{JrGeRdDwJJGhAoCtBsENOVK\\?TDXFLADARFd@Rd@`@zElEdXrVhGzFpDhDZT|BrBvDpDjBdBhD`D`DtC^`@BDFDB@pDfDtPtOjQhPpKzJhBdBlFbFb@XxAtAbGxF' """
        f.write(polyline + ");")
        f.write("\n")
        f.write(""" var decodedLevels = decodeLevels("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");

                var setRegion = new google.maps.Polyline({
                    path: decodedPath,
                    levels: decodedLevels,
                    strokeColor: "#FF0000",
                    strokeOpacity: 1.0,
                    strokeWeight: 2,
                    map: map
                });
            }

            function decodeLevels(encodedLevelsString) {
                var decodedLevels = [];

                for (var i = 0; i < encodedLevelsString.length; ++i) {
                    var level = encodedLevelsString.charCodeAt(i) - 63;
                    decodedLevels.push(level);
                }
                return decodedLevels;
            }
        </script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/common.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/util.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/map.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/poly.js"></script>
        <style type="text/css">
            .gm-style {
                font: 400 11px Roboto, Arial, sans-serif;
                text-decoration: none;
            }

            .gm-style img {
                max-width: none;
            }
        </style>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/onion.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/controls.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/marker.js"></script>
        <script type="text/javascript" charset="UTF-8" src="http://maps.google.com/maps-api-v3/api/js/33/3/stats.js"></script> """)

        f.write("</head>")

        f.write(""" <body onload="initialize()"> """)

        f.write("""

                    <table border="0" width="100%" cellpadding="10">
            <tbody>
                <tr>

                    <td width="50%" valign="top">
                        <div id="map" style="position: relative; overflow: hidden;">
                            <div style="height: 100%; width: 100%; position: absolute; top: 0px; left: 0px; background-color: rgb(229, 227, 223);">
                                <div class="gm-style" style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px;">
                                    <div tabindex="0" style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; cursor: url(http://maps.gstatic.com/mapfiles/openhand_8_8.cur), default;">
                                        <div style="z-index: 1; position: absolute; left: 50%; top: 50%; transform: translate(0px, 0px);">
                                            <div style="position: absolute; left: 0px; top: 0px; z-index: 100; width: 100%;">
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 0;">
                                                    <div style="position: absolute; z-index: 1; transform: matrix(1, 0, 0, 1, -29, -235);">
                                                        <div style="position: absolute; left: 0px; top: 256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -256px; top: 256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -256px; top: 0px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 0px; top: 0px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 256px; top: 0px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 256px; top: 256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 256px; top: 512px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 0px; top: 512px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -256px; top: 512px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -512px; top: 512px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -512px; top: 256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -512px; top: 0px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -512px; top: -256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: -256px; top: -256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 0px; top: -256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                        <div style="position: absolute; left: 256px; top: -256px; width: 256px; height: 256px;">
                                                            <div style="width: 256px; height: 256px;"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div style="position: absolute; left: 0px; top: 0px; z-index: 101; width: 100%;">
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 30;">
                                                    <div style="position: absolute; z-index: 1; transform: matrix(1, 0, 0, 1, -29, -235);">
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 0px; top: 256px;"><canvas width="512" height="512" draggable="false" style="width: 256px; height: 256px; -webkit-user-select: none; position: absolute; left: 0px; top: 0px;"></canvas></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -256px; top: 256px;"><canvas width="512" height="512" draggable="false" style="width: 256px; height: 256px; -webkit-user-select: none; position: absolute; left: 0px; top: 0px;"></canvas></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -256px; top: 0px;"><canvas width="512" height="512" draggable="false" style="width: 256px; height: 256px; -webkit-user-select: none; position: absolute; left: 0px; top: 0px;"></canvas></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 0px; top: 0px;"><canvas width="512" height="512" draggable="false" style="width: 256px; height: 256px; -webkit-user-select: none; position: absolute; left: 0px; top: 0px;"></canvas></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 256px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 256px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -256px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 0px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 256px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -512px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -512px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -512px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 256px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: 0px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -256px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; position: absolute; left: -512px; top: 512px;"></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div style="position: absolute; left: 0px; top: 0px; z-index: 102; width: 100%;"></div>
                                            <div style="position: absolute; left: 0px; top: 0px; z-index: 103; width: 100%;">
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: -1;">
                                                    <div style="position: absolute; z-index: 1; transform: matrix(1, 0, 0, 1, -29, -235);">
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 0px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -256px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -256px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 0px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 256px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 256px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -256px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 0px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 256px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -512px; top: 256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -512px; top: 0px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -512px; top: -256px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 256px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: 0px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -256px; top: 512px;"></div>
                                                        <div style="width: 256px; height: 256px; overflow: hidden; position: absolute; left: -512px; top: 512px;"></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div style="position: absolute; left: 0px; top: 0px; z-index: 0;">
                                                <div style="position: absolute; z-index: 1; transform: matrix(1, 0, 0, 1, -29, -235);">
                                                    <div style="position: absolute; left: 0px; top: 256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i744!3i1174!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=57073"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -256px; top: 256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i743!3i1174!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=34185"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -256px; top: 0px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i743!3i1173!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=84738"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 0px; top: 0px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i744!3i1173!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=107626"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 256px; top: 0px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i745!3i1173!4i256!2m3!1e0!2sm!3i424125876!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=113365"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 256px; top: 256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i745!3i1174!4i256!2m3!1e0!2sm!3i424125876!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=62812"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -512px; top: 256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i742!3i1174!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=11297"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -512px; top: 0px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i742!3i1173!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=61850"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -512px; top: -256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i742!3i1172!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=112403"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -256px; top: -256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i743!3i1172!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=4220"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 0px; top: -256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i744!3i1172!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=27108"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 256px; top: -256px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i745!3i1172!4i256!2m3!1e0!2sm!3i424125876!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=32847"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 256px; top: 512px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i745!3i1175!4i256!2m3!1e0!2sm!3i424125720!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=94615"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: 0px; top: 512px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i744!3i1175!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=6520"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -256px; top: 512px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i743!3i1175!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=114703"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                    <div style="position: absolute; left: -512px; top: 512px; width: 256px; height: 256px;"><img draggable="false" alt="" src="http://maps.google.com/maps/vt?pb=!1m5!1m4!1i11!2i742!3i1175!4i256!2m3!1e0!2sm!3i424125948!3m9!2sen-US!3sUS!5e18!12m1!1e68!12m3!1e37!2m1!1ssmartmaps!4e0!5m1!5f2!23i1301875&amp;token=91815"
                                                            style="width: 256px; height: 256px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="gm-style-pbc" style="z-index: 2; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px; transition-duration: 0.2s; opacity: 0;">
                                            <p class="gm-style-pbt"></p>
                                        </div>
                                        <div style="z-index: 3; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px;">
                                            <div style="z-index: 1; position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px;"></div>
                                            <div style="z-index: 4; position: absolute; left: 50%; top: 50%; transform: translate(0px, 0px);">
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 104; width: 100%;"></div>
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 105; width: 100%;"></div>
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 106; width: 100%;"></div>
                                                <div style="position: absolute; left: 0px; top: 0px; z-index: 107; width: 100%;">
                                                    <div style="z-index: -202; cursor: pointer; display: none;">
                                                        <div style="width: 30px; height: 27px; overflow: hidden; position: absolute;"><img alt="" src="http://maps.gstatic.com/mapfiles/undo_poly.png" draggable="false" style="position: absolute; left: 0px; top: 0px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 90px; height: 27px;"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div><iframe frameborder="0" src="about:blank" style="z-index: -1; position: absolute; width: 100%; height: 100%; top: 0px; left: 0px; border: none;"></iframe>
                                    <div style="margin-left: 5px; margin-right: 5px; z-index: 1000000; position: absolute; left: 0px; bottom: 0px;">
                                        <a target="_blank" href="https://maps.google.com/maps?ll=-22.907104,-47.06324&amp;z=10&amp;t=m&amp;hl=en-US&amp;gl=US&amp;mapclient=apiv3" title="Click to see this area on Google Maps" style="position: static; overflow: visible; float: none; display: inline;">
                                            <div style="width: 66px; height: 26px; cursor: pointer;"><img alt="" src="https://maps.gstatic.com/mapfiles/api-3/images/google4_hdpi.png" draggable="false" style="position: absolute; left: 0px; top: 0px; width: 66px; height: 26px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px;"></div>
                                        </a>
                                    </div>
                                    <div style="background-color: white; padding: 15px 21px; border: 1px solid rgb(171, 171, 171); font-family: Roboto, Arial, sans-serif; color: rgb(34, 34, 34); -webkit-box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 16px; box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 16px; z-index: 10000002; display: none; width: 256px; height: 148px; position: absolute; left: 185px; top: 210px;">
                                        <div style="padding: 0px 0px 10px; font-size: 16px;">Map Data</div>
                                        <div style="font-size: 13px;">Map data ©2018 Google</div>
                                        <div style="width: 13px; height: 13px; overflow: hidden; position: absolute; opacity: 0.7; right: 12px; top: 12px; z-index: 10000; cursor: pointer;"><img alt="" src="https://maps.gstatic.com/mapfiles/api-3/images/mapcnt6.png" draggable="false" style="position: absolute; left: -2px; top: -336px; width: 59px; height: 492px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                    </div>
                                    <div class="gmnoprint" style="z-index: 1000001; position: absolute; right: 166px; bottom: 0px; width: 121px;">
                                        <div draggable="false" class="gm-style-cc" style="-webkit-user-select: none; height: 14px; line-height: 14px;">
                                            <div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;">
                                                <div style="width: 1px;"></div>
                                                <div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div>
                                            </div>
                                            <div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a style="text-decoration: none; cursor: pointer; display: none;">Map Data</a><span>Map data ©2018 Google</span></div>
                                        </div>
                                    </div>
                                    <div class="gmnoscreen" style="position: absolute; right: 0px; bottom: 0px;">
                                        <div style="font-family: Roboto, Arial, sans-serif; font-size: 11px; color: rgb(68, 68, 68); direction: ltr; text-align: right; background-color: rgb(245, 245, 245);">Map data ©2018 Google</div>
                                    </div>
                                    <div class="gmnoprint gm-style-cc" draggable="false" style="z-index: 1000001; -webkit-user-select: none; height: 14px; line-height: 14px; position: absolute; right: 95px; bottom: 0px;">
                                        <div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;">
                                            <div style="width: 1px;"></div>
                                            <div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div>
                                        </div>
                                        <div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a href="https://www.google.com/intl/en-US_US/help/terms_maps.html" target="_blank" style="text-decoration: none; cursor: pointer; color: rgb(68, 68, 68);">Terms of Use</a></div>
                                    </div><button draggable="false" title="Toggle fullscreen view" aria-label="Toggle fullscreen view" type="button" style="background-image: none; background-color: rgb(255, 255, 255); border: 0px; margin: 10px 14px; padding: 0px; position: absolute; cursor: pointer; -webkit-user-select: none; width: 25px; height: 25px; overflow: hidden; top: 0px; right: 0px; background-position: initial initial; background-repeat: initial initial;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/sv9.png" draggable="false" class="gm-fullscreen-control" style="position: absolute; left: -52px; top: -86px; width: 164px; height: 175px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px;"></button>
                                    <div
                                        draggable="false" class="gm-style-cc" style="-webkit-user-select: none; height: 14px; line-height: 14px; position: absolute; right: 0px; bottom: 0px;">
                                        <div style="opacity: 0.7; width: 100%; height: 100%; position: absolute;">
                                            <div style="width: 1px;"></div>
                                            <div style="background-color: rgb(245, 245, 245); width: auto; height: 100%; margin-left: 1px;"></div>
                                        </div>
                                        <div style="position: relative; padding-right: 6px; padding-left: 6px; font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); white-space: nowrap; direction: ltr; text-align: right; vertical-align: middle; display: inline-block;"><a target="_blank" rel="noopener" title="Report errors in the road map or imagery to Google" href="https://www.google.com/maps/@-25.4702013,-49.1985364,11z/data=!10m1!1e1!12b1?source=apiv3&amp;rapsrc=apiv3" style="font-family: Roboto, Arial, sans-serif; font-size: 10px; color: rgb(68, 68, 68); text-decoration: none; position: relative;">Report a map error</a></div>
                                </div>
                                <div class="gmnoprint gm-bundled-control gm-bundled-control-on-bottom" draggable="false" controlwidth="28" controlheight="93" style="margin: 10px; -webkit-user-select: none; position: absolute; bottom: 107px; right: 28px;">
                                    <div class="gmnoprint" controlwidth="28" controlheight="55" style="position: absolute; left: 0px; top: 38px;">
                                        <div draggable="false" style="-webkit-user-select: none; -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-right-radius: 2px; border-bottom-left-radius: 2px; cursor: pointer; background-color: rgb(255, 255, 255); width: 28px; height: 55px;"><button draggable="false" title="Zoom in" aria-label="Zoom in" type="button" style="background-image: none; display: block; border: 0px; margin: 0px; padding: 0px; position: relative; cursor: pointer; -webkit-user-select: none; width: 28px; height: 27px; top: 0px; left: 0px; background-position: initial initial; background-repeat: initial initial;"><div style="overflow: hidden; position: absolute; width: 15px; height: 15px; left: 7px; top: 6px;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/tmapctrl_hdpi.png" draggable="false" style="position: absolute; left: 0px; top: 0px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 120px; height: 54px;"></div></button>
                                            <div
                                                style="position: relative; overflow: hidden; width: 67%; height: 1px; left: 16%; background-color: rgb(230, 230, 230); top: 0px;"></div><button draggable="false" title="Zoom out" aria-label="Zoom out" type="button" style="background-image: none; display: block; border: 0px; margin: 0px; padding: 0px; position: relative; cursor: pointer; -webkit-user-select: none; width: 28px; height: 27px; top: 0px; left: 0px; background-position: initial initial; background-repeat: initial initial;"><div style="overflow: hidden; position: absolute; width: 15px; height: 15px; left: 7px; top: 6px;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/tmapctrl_hdpi.png" draggable="false" style="position: absolute; left: 0px; top: -15px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 120px; height: 54px;"></div></button></div>
                                </div>
                                <div class="gm-svpc" controlwidth="28" controlheight="28" style="background-color: rgb(255, 255, 255); -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-right-radius: 2px; border-bottom-left-radius: 2px; width: 28px; height: 28px; cursor: url(http://maps.gstatic.com/mapfiles/openhand_8_8.cur), default; position: absolute; left: 0px; top: 0px;">
                                    <div style="position: absolute; left: 1px; top: 1px;"></div>
                                    <div style="position: absolute; left: 1px; top: 1px;">
                                        <div aria-label="Street View Pegman Control" style="width: 26px; height: 26px; overflow: hidden; position: absolute; left: 0px; top: 0px;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/cb_scout5_hdpi.png" draggable="false" style="position: absolute; left: -147px; top: -26px; width: 215px; height: 835px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                        <div
                                            aria-label="Pegman is on top of the Map" style="width: 26px; height: 26px; overflow: hidden; position: absolute; left: 0px; top: 0px; visibility: hidden;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/cb_scout5_hdpi.png" draggable="false" style="position: absolute; left: -147px; top: -52px; width: 215px; height: 835px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                                    <div
                                        aria-label="Street View Pegman Control" style="width: 26px; height: 26px; overflow: hidden; position: absolute; left: 0px; top: 0px; visibility: hidden;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/cb_scout5_hdpi.png" draggable="false" style="position: absolute; left: -147px; top: -78px; width: 215px; height: 835px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                            </div>
                        </div>
                        <div class="gmnoprint" controlwidth="28" controlheight="0" style="display: none; position: absolute;">
                            <div title="Rotate map 90 degrees" style="width: 28px; height: 28px; overflow: hidden; position: absolute; background-color: rgb(255, 255, 255); -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-right-radius: 2px; border-bottom-left-radius: 2px; cursor: pointer; display: none;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/tmapctrl4_hdpi.png" draggable="false" style="position: absolute; left: -141px; top: 6px; width: 170px; height: 54px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                            <div
                                class="gm-tilt" style="width: 28px; height: 28px; overflow: hidden; position: absolute; background-color: rgb(255, 255, 255); -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; border-top-left-radius: 2px; border-top-right-radius: 2px; border-bottom-right-radius: 2px; border-bottom-left-radius: 2px; top: 0px; cursor: pointer;"><img alt="" src="http://maps.gstatic.com/mapfiles/api-3/images/tmapctrl4_hdpi.png" draggable="false" style="position: absolute; left: -141px; top: -13px; width: 170px; height: 54px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none;"></div>
                        </div>
                        </div>
                        <div class="gmnoprint" style="margin: 10px; z-index: 0; position: absolute; cursor: pointer; left: 0px; top: 0px;">
                            <div class="gm-style-mtc" style="float: left; position: relative;">
                                <div role="button" tabindex="0" title="Show street map" aria-label="Show street map" aria-pressed="true" draggable="false" style="direction: ltr; overflow: hidden; text-align: center; position: relative; color: rgb(0, 0, 0); font-family: Roboto, Arial, sans-serif; -webkit-user-select: none; font-size: 11px; background-color: rgb(255, 255, 255); padding: 8px; border-bottom-left-radius: 2px; border-top-left-radius: 2px; -webkit-background-clip: padding-box; background-clip: padding-box; -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; min-width: 21px; font-weight: 500;">Map</div>
                                <div style="background-color: white; z-index: -1; padding: 2px; border-bottom-left-radius: 2px; border-bottom-right-radius: 2px; -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; position: absolute; left: 0px; top: 29px; text-align: left; display: none;">
                                    <div draggable="false" title="Show street map with terrain" style="color: rgb(0, 0, 0); font-family: Roboto, Arial, sans-serif; -webkit-user-select: none; font-size: 11px; background-color: rgb(255, 255, 255); padding: 6px 8px 6px 6px; direction: ltr; text-align: left; white-space: nowrap;"><span role="checkbox" style="box-sizing: border-box; position: relative; line-height: 0; font-size: 0px; margin: 0px 5px 0px 0px; display: inline-block; background-color: rgb(255, 255, 255); border: 1px solid rgb(198, 198, 198); border-top-left-radius: 1px; border-top-right-radius: 1px; border-bottom-right-radius: 1px; border-bottom-left-radius: 1px; width: 13px; height: 13px; vertical-align: middle;"><div style="position: absolute; left: 1px; top: -2px; width: 13px; height: 11px; overflow: hidden; display: none;"><img alt="" src="http://maps.gstatic.com/mapfiles/mv/imgs8.png" draggable="false" style="position: absolute; left: -52px; top: -44px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 68px; height: 67px;"></div></span>
                                        <label
                                            style="vertical-align: middle; cursor: pointer;">Terrain</label>
                                    </div>
                                </div>
                            </div>
                            <div class="gm-style-mtc" style="float: left; position: relative;">
                                <div role="button" tabindex="0" title="Show satellite imagery" aria-label="Show satellite imagery" aria-pressed="false" draggable="false" style="direction: ltr; overflow: hidden; text-align: center; position: relative; color: rgb(86, 86, 86); font-family: Roboto, Arial, sans-serif; -webkit-user-select: none; font-size: 11px; background-color: rgb(255, 255, 255); padding: 8px; border-bottom-right-radius: 2px; border-top-right-radius: 2px; -webkit-background-clip: padding-box; background-clip: padding-box; -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; min-width: 39px; border-left-width: 0px;">Satellite</div>
                                <div style="background-color: white; z-index: -1; padding: 2px; border-bottom-left-radius: 2px; border-bottom-right-radius: 2px; -webkit-box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; box-shadow: rgba(0, 0, 0, 0.298039) 0px 1px 4px -1px; position: absolute; right: 0px; top: 29px; text-align: left; display: none;">
                                    <div draggable="false" title="Show imagery with street names" style="color: rgb(0, 0, 0); font-family: Roboto, Arial, sans-serif; -webkit-user-select: none; font-size: 11px; background-color: rgb(255, 255, 255); padding: 6px 8px 6px 6px; direction: ltr; text-align: left; white-space: nowrap;"><span role="checkbox" style="box-sizing: border-box; position: relative; line-height: 0; font-size: 0px; margin: 0px 5px 0px 0px; display: inline-block; background-color: rgb(255, 255, 255); border: 1px solid rgb(198, 198, 198); border-top-left-radius: 1px; border-top-right-radius: 1px; border-bottom-right-radius: 1px; border-bottom-left-radius: 1px; width: 13px; height: 13px; vertical-align: middle;"><div style="position: absolute; left: 1px; top: -2px; width: 13px; height: 11px; overflow: hidden;"><img alt="" src="http://maps.gstatic.com/mapfiles/mv/imgs8.png" draggable="false" style="position: absolute; left: -52px; top: -44px; -webkit-user-select: none; border: 0px; padding: 0px; margin: 0px; max-width: none; width: 68px; height: 67px;"></div></span>
                                        <label
                                            style="vertical-align: middle; cursor: pointer;">Labels</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                        </div>
                        </div>
                    </td>

                    <td width="50%" valign="top">
                        <h1>About trip: </h1>


                        <table border="0" width="100%" cellpadding="10">
                            <tbody>
                                <tr>

                """)
        f.write("""
            <td width="5%" valign="top">
            <h5 align="CENTER">Index: </h5>
            <p align="CENTER">
            <font size="2">1</font>
            </p>
            <p align="CENTER">
            <font size="2">2</font>
            </p>
            </td>
            """)

        f.write(""" <td width="20%" valign="top">
                                        <h5 align="CENTER">Points: </h5>
                                        <palign=center> """)
        # lat_init, lng_init = -25.3491784, -49.1640331
        # lat_fim, lng_fim = -25.3882016, -49.2056257
        f.write("""<font size="2"> """ + str(lat_init) + " , " + str(lng_init) + """ </font> """)
        f.write("""<p></p>
                <palign=center>""")

        f.write("""<font size="2"> """ + str(lat_fim) + " , " + str(lng_fim) + """ </font> """)
        f.write(""" <p></p>
                    </palign=center>
                    </td> """)
        f.write("""<td width="10%" valign="top">
                    <h5 align="CENTER">Distance (m): </h5>
                    <p align="CENTER">""")
        # distance = 6654
        f.write(""" <font size="2">"""  + str(distance) + """</font>""")
        f.write(""" </p>
                    </td>
                    <td width="15%" valign="top">
                    <h5 align="CENTER">Time of trip (s): </h5>
                    <p align="CENTER">
                """)
        # time_of_trip = 19
        f.write(""" <font size="2"> """ + str(time_of_trip) + "</font>")
        f.write(""" </p>
                    </td>
                    </tr>
                    </tbody>
                    </table>
                    <hr> """)
        # timestamp = "14/02/98"
        f.write(""" <h5 align="LEFT"> GMT Time: """ + str(timestamp) + "</h5")
        f.write("<br></br>")
        # traffic = 63
        f.write(""" <h5 align="LEFT"> Duration in traffic (s): """ + str(traffic) + "</h5")
        f.write("<br></br>")
        # duration = 10
        # dist = 10
        f.write(""" <h5 align="LEFT"> Distance (m): """ + str(dist) + "</h5")
        f.write("<br></br>")

        f.write(""" </td>
                </tr>
                </tbody>
                </table> """)

        f.write("</body>")

        f.write("</html>")


        f.close()
