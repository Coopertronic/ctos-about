# Maintainer: Matthew Phillip Cooper <coopertronics@gmail.com>

pkgname=about
pkgver=1
pkgrel=1
pkgdesc="This is the about dialog for Coopertronic OS. It givs a breif overview of what Coopertronic OS is all about."
arch=('any')
url="https://www.emuparadise.me/ScummVM_Games/Discworld_2_(CD_DOS)/95799"
gmpkgurl="https://coopertronic-ws.ddns.net/ctos-assets/"
license=('custom')
depends=('scummvm')
source=("$gmpkgurl$pkgname/$pkgname-v$pkgver.zip"
  "$gmpkgurl$pkgname/$pkgname.sh"
  "$gmpkgurl$pkgname/org.$pkgname.$pkgname.svg"
  "$gmpkgurl$pkgname/org.$pkgname.$pkgname.desktop")
md5sums=('4745f767361e97eddbe6cee2beec1182'
  '78ad89da79646086cd5317cca3974c85'
  'a1b67466b6936f8ee936a1f5f2780879'
  'a8e85b4bd8d8aa0fff028487408313bb')

package() {
  ##  Install documentation
  #install -D -m644 $srcdir/README $pkgdir/usr/share/doc/$pkgname/README

  ##  Install licenses
  #install -d $pkgdir/usr/share/licenses/$pkgname
  #install -m644 $srcdir/license-* $pkgdir/usr/share/licenses/$pkgname/

  ##  Install binaries
  install -d $pkgdir/usr/share/$pkgname
  install -D -m644 $srcdir/$pkgname-v$pkgver/* $pkgdir/usr/share/$pkgname/
  install -D -m755 $pkgname.sh $pkgdir/usr/bin/$pkgname

  ##  Install game icon
  install -d $pkgdir/usr/share/icons/hicolor/scalable/apps
  install -D -m644 org.$pkgname.$pkgname.svg $pkgdir/usr/share/icons/hicolor/scalable/apps/org.$pkgname.$pkgname.svg

  ##  Install Application desktop launcher
  install -d $pkgdir/usr/share/applications
  install -D -m644 org.$pkgname.$pkgname.desktop $pkgdir/usr/share/applications/org.$pkgname.$pkgname.desktop
}
