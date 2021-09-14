/*
 * filter registration
 * Copyright (c) 2008 Vitor Sessak
 *
 * This file is part of FFmpeg.
 *
 * FFmpeg is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * FFmpeg is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with FFmpeg; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

#include "libavutil/thread.h"
#include "avfilter.h"
#include "config.h"

extern const AVFilter ff_af_abench;
extern const AVFilter ff_af_acompressor;
extern const AVFilter ff_af_acontrast;
extern const AVFilter ff_af_acopy;
extern const AVFilter ff_af_acue;
extern const AVFilter ff_af_acrossfade;
extern const AVFilter ff_af_acrossover;
extern const AVFilter ff_af_acrusher;
extern const AVFilter ff_af_adeclick;
extern const AVFilter ff_af_adeclip;
extern const AVFilter ff_af_adecorrelate;
extern const AVFilter ff_af_adelay;
extern const AVFilter ff_af_adenorm;
extern const AVFilter ff_af_aderivative;
extern const AVFilter ff_af_aecho;
extern const AVFilter ff_af_aemphasis;
extern const AVFilter ff_af_aeval;
extern const AVFilter ff_af_aexciter;
extern const AVFilter ff_af_afade;
extern const AVFilter ff_af_afftdn;
extern const AVFilter ff_af_afftfilt;
extern const AVFilter ff_af_afir;
extern const AVFilter ff_af_aformat;
extern const AVFilter ff_af_afreqshift;
extern const AVFilter ff_af_afwtdn;
extern const AVFilter ff_af_agate;
extern const AVFilter ff_af_aiir;
extern const AVFilter ff_af_aintegral;
extern const AVFilter ff_af_ainterleave;
extern const AVFilter ff_af_alimiter;
extern const AVFilter ff_af_allpass;
extern const AVFilter ff_af_aloop;
extern const AVFilter ff_af_amerge;
extern const AVFilter ff_af_ametadata;
extern const AVFilter ff_af_amix;
extern const AVFilter ff_af_amultiply;
extern const AVFilter ff_af_anequalizer;
extern const AVFilter ff_af_anlmdn;
extern const AVFilter ff_af_anlms;
extern const AVFilter ff_af_anull;
extern const AVFilter ff_af_apad;
extern const AVFilter ff_af_aperms;
extern const AVFilter ff_af_aphaser;
extern const AVFilter ff_af_aphaseshift;
extern const AVFilter ff_af_apsyclip;
extern const AVFilter ff_af_apulsator;
extern const AVFilter ff_af_arealtime;
extern const AVFilter ff_af_aresample;
extern const AVFilter ff_af_areverse;
extern const AVFilter ff_af_arnndn;
extern const AVFilter ff_af_asegment;
extern const AVFilter ff_af_aselect;
extern const AVFilter ff_af_asendcmd;
extern const AVFilter ff_af_asetnsamples;
extern const AVFilter ff_af_asetpts;
extern const AVFilter ff_af_asetrate;
extern const AVFilter ff_af_asettb;
extern const AVFilter ff_af_ashowinfo;
extern const AVFilter ff_af_asidedata;
extern const AVFilter ff_af_asoftclip;
extern const AVFilter ff_af_asplit;
extern const AVFilter ff_af_asr;
extern const AVFilter ff_af_astats;
extern const AVFilter ff_af_astreamselect;
extern const AVFilter ff_af_asubboost;
extern const AVFilter ff_af_asubcut;
extern const AVFilter ff_af_asupercut;
extern const AVFilter ff_af_asuperpass;
extern const AVFilter ff_af_asuperstop;
extern const AVFilter ff_af_atempo;
extern const AVFilter ff_af_atilt;
extern const AVFilter ff_af_atrim;
extern const AVFilter ff_af_axcorrelate;
extern const AVFilter ff_af_azmq;
extern const AVFilter ff_af_bandpass;
extern const AVFilter ff_af_bandreject;
extern const AVFilter ff_af_bass;
extern const AVFilter ff_af_biquad;
extern const AVFilter ff_af_bs2b;
extern const AVFilter ff_vf_chromaber_vulkan;
extern const AVFilter ff_af_channelmap;
extern const AVFilter ff_af_channelsplit;
extern const AVFilter ff_af_chorus;
extern const AVFilter ff_af_compand;
extern const AVFilter ff_af_compensationdelay;
extern const AVFilter ff_af_crossfeed;
extern const AVFilter ff_af_crystalizer;
extern const AVFilter ff_af_dcshift;
extern const AVFilter ff_af_deesser;
extern const AVFilter ff_af_drmeter;
extern const AVFilter ff_af_dynaudnorm;
extern const AVFilter ff_af_earwax;
extern const AVFilter ff_af_ebur128;
extern const AVFilter ff_af_equalizer;
extern const AVFilter ff_af_extrastereo;
extern const AVFilter ff_af_firequalizer;
extern const AVFilter ff_af_flanger;
extern const AVFilter ff_af_haas;
extern const AVFilter ff_af_hdcd;
extern const AVFilter ff_af_headphone;
extern const AVFilter ff_af_highpass;
extern const AVFilter ff_af_highshelf;
extern const AVFilter ff_af_join;
extern const AVFilter ff_af_ladspa;
extern const AVFilter ff_af_loudnorm;
extern const AVFilter ff_af_lowpass;
extern const AVFilter ff_af_lowshelf;
extern const AVFilter ff_af_lv2;
extern const AVFilter ff_af_mcompand;
extern const AVFilter ff_af_pan;
extern const AVFilter ff_af_replaygain;
extern const AVFilter ff_af_rubberband;
extern const AVFilter ff_af_sidechaincompress;
extern const AVFilter ff_af_sidechaingate;
extern const AVFilter ff_af_silencedetect;
extern const AVFilter ff_af_silenceremove;
extern const AVFilter ff_af_sofalizer;
extern const AVFilter ff_af_speechnorm;
extern const AVFilter ff_af_stereotools;
extern const AVFilter ff_af_stereowiden;
extern const AVFilter ff_af_superequalizer;
extern const AVFilter ff_af_surround;
extern const AVFilter ff_af_treble;
extern const AVFilter ff_af_tremolo;
extern const AVFilter ff_af_vibrato;
extern const AVFilter ff_af_volume;
extern const AVFilter ff_af_volumedetect;

extern const AVFilter ff_asrc_aevalsrc;
extern const AVFilter ff_asrc_afirsrc;
extern const AVFilter ff_asrc_anoisesrc;
extern const AVFilter ff_asrc_anullsrc;
extern const AVFilter ff_asrc_flite;
extern const AVFilter ff_asrc_hilbert;
extern const AVFilter ff_asrc_sinc;
extern const AVFilter ff_asrc_sine;

extern const AVFilter ff_asink_anullsink;

extern const AVFilter ff_vf_addroi;
extern const AVFilter ff_vf_alphaextract;
extern const AVFilter ff_vf_alphamerge;
extern const AVFilter ff_vf_amplify;
extern const AVFilter ff_vf_ass;
extern const AVFilter ff_vf_atadenoise;
extern const AVFilter ff_vf_avgblur;
extern const AVFilter ff_vf_avgblur_opencl;
extern const AVFilter ff_vf_avgblur_vulkan;
extern const AVFilter ff_vf_bbox;
extern const AVFilter ff_vf_bench;
extern const AVFilter ff_vf_bilateral;
extern const AVFilter ff_vf_bitplanenoise;
extern const AVFilter ff_vf_blackdetect;
extern const AVFilter ff_vf_blackframe;
extern const AVFilter ff_vf_blend;
extern const AVFilter ff_vf_bm3d;
extern const AVFilter ff_vf_boxblur;
extern const AVFilter ff_vf_boxblur_opencl;
extern const AVFilter ff_vf_bwdif;
extern const AVFilter ff_vf_cas;
extern const AVFilter ff_vf_chromahold;
extern const AVFilter ff_vf_chromakey;
extern const AVFilter ff_vf_chromanr;
extern const AVFilter ff_vf_chromashift;
extern const AVFilter ff_vf_ciescope;
extern const AVFilter ff_vf_codecview;
extern const AVFilter ff_vf_colorbalance;
extern const AVFilter ff_vf_colorchannelmixer;
extern const AVFilter ff_vf_colorcontrast;
extern const AVFilter ff_vf_colorcorrect;
extern const AVFilter ff_vf_colorize;
extern const AVFilter ff_vf_colorkey;
extern const AVFilter ff_vf_colorkey_opencl;
extern const AVFilter ff_vf_colorhold;
extern const AVFilter ff_vf_colorlevels;
extern const AVFilter ff_vf_colormatrix;
extern const AVFilter ff_vf_colorspace;
extern const AVFilter ff_vf_colortemperature;
extern const AVFilter ff_vf_convolution;
extern const AVFilter ff_vf_convolution_opencl;
extern const AVFilter ff_vf_convolve;
extern const AVFilter ff_vf_copy;
extern const AVFilter ff_vf_coreimage;
extern const AVFilter ff_vf_cover_rect;
extern const AVFilter ff_vf_crop;
extern const AVFilter ff_vf_cropdetect;
extern const AVFilter ff_vf_cue;
extern const AVFilter ff_vf_curves;
extern const AVFilter ff_vf_datascope;
extern const AVFilter ff_vf_dblur;
extern const AVFilter ff_vf_dctdnoiz;
extern const AVFilter ff_vf_deband;
extern const AVFilter ff_vf_deblock;
extern const AVFilter ff_vf_decimate;
extern const AVFilter ff_vf_deconvolve;
extern const AVFilter ff_vf_dedot;
extern const AVFilter ff_vf_deflate;
extern const AVFilter ff_vf_deflicker;
extern const AVFilter ff_vf_deinterlace_qsv;
extern const AVFilter ff_vf_deinterlace_vaapi;
extern const AVFilter ff_vf_dejudder;
extern const AVFilter ff_vf_delogo;
extern const AVFilter ff_vf_denoise_vaapi;
extern const AVFilter ff_vf_derain;
extern const AVFilter ff_vf_deshake;
extern const AVFilter ff_vf_deshake_opencl;
extern const AVFilter ff_vf_despill;
extern const AVFilter ff_vf_detelecine;
extern const AVFilter ff_vf_dilation;
extern const AVFilter ff_vf_dilation_opencl;
extern const AVFilter ff_vf_displace;
extern const AVFilter ff_vf_dnn_classify;
extern const AVFilter ff_vf_dnn_detect;
extern const AVFilter ff_vf_dnn_processing;
extern const AVFilter ff_vf_doubleweave;
extern const AVFilter ff_vf_drawbox;
extern const AVFilter ff_vf_drawgraph;
extern const AVFilter ff_vf_drawgrid;
extern const AVFilter ff_vf_drawtext;
extern const AVFilter ff_vf_edgedetect;
extern const AVFilter ff_vf_elbg;
extern const AVFilter ff_vf_entropy;
extern const AVFilter ff_vf_epx;
extern const AVFilter ff_vf_eq;
extern const AVFilter ff_vf_erosion;
extern const AVFilter ff_vf_erosion_opencl;
extern const AVFilter ff_vf_estdif;
extern const AVFilter ff_vf_exposure;
extern const AVFilter ff_vf_extractplanes;
extern const AVFilter ff_vf_fade;
extern const AVFilter ff_vf_fftdnoiz;
extern const AVFilter ff_vf_fftfilt;
extern const AVFilter ff_vf_field;
extern const AVFilter ff_vf_fieldhint;
extern const AVFilter ff_vf_fieldmatch;
extern const AVFilter ff_vf_fieldorder;
extern const AVFilter ff_vf_fillborders;
extern const AVFilter ff_vf_find_rect;
extern const AVFilter ff_vf_floodfill;
extern const AVFilter ff_vf_format;
extern const AVFilter ff_vf_fps;
extern const AVFilter ff_vf_framepack;
extern const AVFilter ff_vf_framerate;
extern const AVFilter ff_vf_framestep;
extern const AVFilter ff_vf_freezedetect;
extern const AVFilter ff_vf_freezeframes;
extern const AVFilter ff_vf_frei0r;
extern const AVFilter ff_vf_fspp;
extern const AVFilter ff_vf_gblur;
extern const AVFilter ff_vf_geq;
extern const AVFilter ff_vf_gradfun;
extern const AVFilter ff_vf_graphmonitor;
extern const AVFilter ff_vf_grayworld;
extern const AVFilter ff_vf_greyedge;
extern const AVFilter ff_vf_guided;
extern const AVFilter ff_vf_haldclut;
extern const AVFilter ff_vf_hflip;
extern const AVFilter ff_vf_histeq;
extern const AVFilter ff_vf_histogram;
extern const AVFilter ff_vf_hqdn3d;
extern const AVFilter ff_vf_hqx;
extern const AVFilter ff_vf_hstack;
extern const AVFilter ff_vf_hsvhold;
extern const AVFilter ff_vf_hsvkey;
extern const AVFilter ff_vf_hue;
extern const AVFilter ff_vf_hwdownload;
extern const AVFilter ff_vf_hwmap;
extern const AVFilter ff_vf_hwupload;
extern const AVFilter ff_vf_hwupload_cuda;
extern const AVFilter ff_vf_hysteresis;
extern const AVFilter ff_vf_identity;
extern const AVFilter ff_vf_idet;
extern const AVFilter ff_vf_il;
extern const AVFilter ff_vf_inflate;
extern const AVFilter ff_vf_interlace;
extern const AVFilter ff_vf_interleave;
extern const AVFilter ff_vf_kerndeint;
extern const AVFilter ff_vf_kirsch;
extern const AVFilter ff_vf_lagfun;
extern const AVFilter ff_vf_lenscorrection;
extern const AVFilter ff_vf_lensfun;
extern const AVFilter ff_vf_libvmaf;
extern const AVFilter ff_vf_limiter;
extern const AVFilter ff_vf_loop;
extern const AVFilter ff_vf_lumakey;
extern const AVFilter ff_vf_lut;
extern const AVFilter ff_vf_lut1d;
extern const AVFilter ff_vf_lut2;
extern const AVFilter ff_vf_lut3d;
extern const AVFilter ff_vf_lutrgb;
extern const AVFilter ff_vf_lutyuv;
extern const AVFilter ff_vf_maskedclamp;
extern const AVFilter ff_vf_maskedmax;
extern const AVFilter ff_vf_maskedmerge;
extern const AVFilter ff_vf_maskedmin;
extern const AVFilter ff_vf_maskedthreshold;
extern const AVFilter ff_vf_maskfun;
extern const AVFilter ff_vf_mcdeint;
extern const AVFilter ff_vf_median;
extern const AVFilter ff_vf_mergeplanes;
extern const AVFilter ff_vf_mestimate;
extern const AVFilter ff_vf_metadata;
extern const AVFilter ff_vf_midequalizer;
extern const AVFilter ff_vf_minterpolate;
extern const AVFilter ff_vf_mix;
extern const AVFilter ff_vf_monochrome;
extern const AVFilter ff_vf_mpdecimate;
extern const AVFilter ff_vf_msad;
extern const AVFilter ff_vf_negate;
extern const AVFilter ff_vf_nlmeans;
extern const AVFilter ff_vf_nlmeans_opencl;
extern const AVFilter ff_vf_nnedi;
extern const AVFilter ff_vf_noformat;
extern const AVFilter ff_vf_noise;
extern const AVFilter ff_vf_normalize;
extern const AVFilter ff_vf_null;
extern const AVFilter ff_vf_ocr;
extern const AVFilter ff_vf_ocv;
extern const AVFilter ff_vf_oscilloscope;
extern const AVFilter ff_vf_overlay;
extern const AVFilter ff_vf_overlay_opencl;
extern const AVFilter ff_vf_overlay_qsv;
extern const AVFilter ff_vf_overlay_vulkan;
extern const AVFilter ff_vf_overlay_cuda;
extern const AVFilter ff_vf_owdenoise;
extern const AVFilter ff_vf_pad;
extern const AVFilter ff_vf_pad_opencl;
extern const AVFilter ff_vf_palettegen;
extern const AVFilter ff_vf_paletteuse;
extern const AVFilter ff_vf_perms;
extern const AVFilter ff_vf_perspective;
extern const AVFilter ff_vf_phase;
extern const AVFilter ff_vf_photosensitivity;
extern const AVFilter ff_vf_pixdesctest;
extern const AVFilter ff_vf_pixscope;
extern const AVFilter ff_vf_pp;
extern const AVFilter ff_vf_pp7;
extern const AVFilter ff_vf_premultiply;
extern const AVFilter ff_vf_prewitt;
extern const AVFilter ff_vf_prewitt_opencl;
extern const AVFilter ff_vf_procamp_vaapi;
extern const AVFilter ff_vf_program_opencl;
extern const AVFilter ff_vf_pseudocolor;
extern const AVFilter ff_vf_psnr;
extern const AVFilter ff_vf_pullup;
extern const AVFilter ff_vf_qp;
extern const AVFilter ff_vf_random;
extern const AVFilter ff_vf_readeia608;
extern const AVFilter ff_vf_readvitc;
extern const AVFilter ff_vf_realtime;
extern const AVFilter ff_vf_remap;
extern const AVFilter ff_vf_removegrain;
extern const AVFilter ff_vf_removelogo;
extern const AVFilter ff_vf_repeatfields;
extern const AVFilter ff_vf_reverse;
extern const AVFilter ff_vf_rgbashift;
extern const AVFilter ff_vf_roberts;
extern const AVFilter ff_vf_roberts_opencl;
extern const AVFilter ff_vf_rotate;
extern const AVFilter ff_vf_sab;
extern const AVFilter ff_vf_scale;
extern const AVFilter ff_vf_scale_cuda;
extern const AVFilter ff_vf_scale_npp;
extern const AVFilter ff_vf_scale_qsv;
extern const AVFilter ff_vf_scale_vaapi;
extern const AVFilter ff_vf_scale_vulkan;
extern const AVFilter ff_vf_scale2ref;
extern const AVFilter ff_vf_scdet;
extern const AVFilter ff_vf_scharr;
extern const AVFilter ff_vf_scroll;
extern const AVFilter ff_vf_segment;
extern const AVFilter ff_vf_select;
extern const AVFilter ff_vf_selectivecolor;
extern const AVFilter ff_vf_sendcmd;
extern const AVFilter ff_vf_separatefields;
extern const AVFilter ff_vf_setdar;
extern const AVFilter ff_vf_setfield;
extern const AVFilter ff_vf_setparams;
extern const AVFilter ff_vf_setpts;
extern const AVFilter ff_vf_setrange;
extern const AVFilter ff_vf_setsar;
extern const AVFilter ff_vf_settb;
extern const AVFilter ff_vf_sharpness_vaapi;
extern const AVFilter ff_vf_shear;
extern const AVFilter ff_vf_showinfo;
extern const AVFilter ff_vf_showpalette;
extern const AVFilter ff_vf_shuffleframes;
extern const AVFilter ff_vf_shufflepixels;
extern const AVFilter ff_vf_shuffleplanes;
extern const AVFilter ff_vf_sidedata;
extern const AVFilter ff_vf_signalstats;
extern const AVFilter ff_vf_signature;
extern const AVFilter ff_vf_smartblur;
extern const AVFilter ff_vf_sobel;
extern const AVFilter ff_vf_sobel_opencl;
extern const AVFilter ff_vf_split;
extern const AVFilter ff_vf_spp;
extern const AVFilter ff_vf_sr;
extern const AVFilter ff_vf_ssim;
extern const AVFilter ff_vf_stereo3d;
extern const AVFilter ff_vf_streamselect;
extern const AVFilter ff_vf_subtitles;
extern const AVFilter ff_vf_super2xsai;
extern const AVFilter ff_vf_swaprect;
extern const AVFilter ff_vf_swapuv;
extern const AVFilter ff_vf_tblend;
extern const AVFilter ff_vf_telecine;
extern const AVFilter ff_vf_thistogram;
extern const AVFilter ff_vf_threshold;
extern const AVFilter ff_vf_thumbnail;
extern const AVFilter ff_vf_thumbnail_cuda;
extern const AVFilter ff_vf_tile;
extern const AVFilter ff_vf_tinterlace;
extern const AVFilter ff_vf_tlut2;
extern const AVFilter ff_vf_tmedian;
extern const AVFilter ff_vf_tmidequalizer;
extern const AVFilter ff_vf_tmix;
extern const AVFilter ff_vf_tonemap;
extern const AVFilter ff_vf_tonemap_opencl;
extern const AVFilter ff_vf_tonemap_vaapi;
extern const AVFilter ff_vf_tpad;
extern const AVFilter ff_vf_transpose;
extern const AVFilter ff_vf_transpose_npp;
extern const AVFilter ff_vf_transpose_opencl;
extern const AVFilter ff_vf_transpose_vaapi;
extern const AVFilter ff_vf_trim;
extern const AVFilter ff_vf_unpremultiply;
extern const AVFilter ff_vf_unsharp;
extern const AVFilter ff_vf_unsharp_opencl;
extern const AVFilter ff_vf_untile;
extern const AVFilter ff_vf_uspp;
extern const AVFilter ff_vf_v360;
extern const AVFilter ff_vf_vaguedenoiser;
extern const AVFilter ff_vf_vectorscope;
extern const AVFilter ff_vf_vflip;
extern const AVFilter ff_vf_vfrdet;
extern const AVFilter ff_vf_vibrance;
extern const AVFilter ff_vf_vidstabdetect;
extern const AVFilter ff_vf_vidstabtransform;
extern const AVFilter ff_vf_vif;
extern const AVFilter ff_vf_vignette;
extern const AVFilter ff_vf_vmafmotion;
extern const AVFilter ff_vf_vpp_qsv;
extern const AVFilter ff_vf_vstack;
extern const AVFilter ff_vf_w3fdif;
extern const AVFilter ff_vf_waveform;
extern const AVFilter ff_vf_weave;
extern const AVFilter ff_vf_xbr;
extern const AVFilter ff_vf_xfade;
extern const AVFilter ff_vf_xfade_opencl;
extern const AVFilter ff_vf_xmedian;
extern const AVFilter ff_vf_xstack;
extern const AVFilter ff_vf_yadif;
extern const AVFilter ff_vf_yadif_cuda;
extern const AVFilter ff_vf_yaepblur;
extern const AVFilter ff_vf_zmq;
extern const AVFilter ff_vf_zoompan;
extern const AVFilter ff_vf_zscale;

extern const AVFilter ff_vsrc_allrgb;
extern const AVFilter ff_vsrc_allyuv;
extern const AVFilter ff_vsrc_cellauto;
extern const AVFilter ff_vsrc_color;
extern const AVFilter ff_vsrc_coreimagesrc;
extern const AVFilter ff_vsrc_frei0r_src;
extern const AVFilter ff_vsrc_gradients;
extern const AVFilter ff_vsrc_haldclutsrc;
extern const AVFilter ff_vsrc_life;
extern const AVFilter ff_vsrc_mandelbrot;
extern const AVFilter ff_vsrc_mptestsrc;
extern const AVFilter ff_vsrc_nullsrc;
extern const AVFilter ff_vsrc_openclsrc;
extern const AVFilter ff_vsrc_pal75bars;
extern const AVFilter ff_vsrc_pal100bars;
extern const AVFilter ff_vsrc_rgbtestsrc;
extern const AVFilter ff_vsrc_sierpinski;
extern const AVFilter ff_vsrc_smptebars;
extern const AVFilter ff_vsrc_smptehdbars;
extern const AVFilter ff_vsrc_testsrc;
extern const AVFilter ff_vsrc_testsrc2;
extern const AVFilter ff_vsrc_yuvtestsrc;

extern const AVFilter ff_vsink_nullsink;

/* multimedia filters */
extern const AVFilter ff_avf_abitscope;
extern const AVFilter ff_avf_adrawgraph;
extern const AVFilter ff_avf_agraphmonitor;
extern const AVFilter ff_avf_ahistogram;
extern const AVFilter ff_avf_aphasemeter;
extern const AVFilter ff_avf_avectorscope;
extern const AVFilter ff_avf_concat;
extern const AVFilter ff_avf_showcqt;
extern const AVFilter ff_avf_showfreqs;
extern const AVFilter ff_avf_showspatial;
extern const AVFilter ff_avf_showspectrum;
extern const AVFilter ff_avf_showspectrumpic;
extern const AVFilter ff_avf_showvolume;
extern const AVFilter ff_avf_showwaves;
extern const AVFilter ff_avf_showwavespic;
extern const AVFilter ff_vaf_spectrumsynth;

/* multimedia sources */
extern const AVFilter ff_avsrc_amovie;
extern const AVFilter ff_avsrc_movie;

/* those filters are part of public or internal API,
 * they are formatted to not be found by the grep
 * as they are manually added again (due to their 'names'
 * being the same while having different 'types'). */
extern  const AVFilter ff_asrc_abuffer;
extern  const AVFilter ff_vsrc_buffer;
extern  const AVFilter ff_asink_abuffer;
extern  const AVFilter ff_vsink_buffer;
extern const AVFilter ff_af_afifo;
extern const AVFilter ff_vf_fifo;

#include "libavfilter/filter_list.c"


const AVFilter *av_filter_iterate(void **opaque)
{
    uintptr_t i = (uintptr_t)*opaque;
    const AVFilter *f = filter_list[i];

    if (f)
        *opaque = (void*)(i + 1);

    return f;
}

const AVFilter *avfilter_get_by_name(const char *name)
{
    const AVFilter *f = NULL;
    void *opaque = 0;

    if (!name)
        return NULL;

    while ((f = av_filter_iterate(&opaque)))
        if (!strcmp(f->name, name))
            return f;

    return NULL;
}
